import { useState, useEffect } from 'react';
import { Button } from "/components/ui/button";
import { Input } from "/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "/components/ui/avatar";

interface User {
  id: string;
  name: string;
  email: string;
  avatar: string;
  status: 'online' | 'offline';
}

interface Message {
  id: string;
  content: string;
  senderId: string;
  receiverId: string;
  timestamp: Date;
  isRead: boolean;
}

interface Group {
  id: string;
  name: string;
  avatar: string;
  lastMessage: string;
  unreadCount: number;
  timestamp: Date;
}

interface Chronicle {
  id: string;
  author: string;
  content: string;
  avatar: string;
  timestamp: Date;
  isViewed: boolean;
}

const App = () => {
  const [currentView, setCurrentView] = useState<'messages' | 'groups' | 'chronicles' | 'me'>('messages');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isRegistering, setIsRegistering] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [searchTerm, setSearchTerm] = useState('');

  // Mock data
  const [users, setUsers] = useState<User[]>([
    {
      id: '1',
      name: 'Sarah Johnson',
      email: 'sarah@example.com',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Professional headshot of a young woman with curly brown hair and friendly smile&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      status: 'online'
    },
    {
      id: '2',
      name: 'Mike Chen',
      email: 'mike@example.com',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Asian man with glasses and professional attire in office setting&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      status: 'online'
    },
    {
      id: '3',
      name: 'Emma Davis',
      email: 'emma@example.com',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Blonde woman with blue eyes and warm smile in casual setting&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      status: 'offline'
    }
  ]);

  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      content: 'Hey! How are you doing today?',
      senderId: '1',
      receiverId: 'current',
      timestamp: new Date(Date.now() - 300000),
      isRead: true
    },
    {
      id: '2',
      content: 'I\'m doing great! Just finished the project',
      senderId: 'current',
      receiverId: '1',
      timestamp: new Date(Date.now() - 240000),
      isRead: true
    },
    {
      id: '3',
      content: 'That\'s awesome! Want to grab coffee later?',
      senderId: '1',
      receiverId: 'current',
      timestamp: new Date(Date.now() - 120000),
      isRead: false
    }
  ]);

  const [groups, setGroups] = useState<Group[]>([
    {
      id: '1',
      name: 'Family Group',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Family silhouette with parents and children holding hands&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      lastMessage: 'Mom: Dinner at 7 PM tonight!',
      unreadCount: 3,
      timestamp: new Date(Date.now() - 3600000)
    },
    {
      id: '2',
      name: 'Work Team',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Team of professionals collaborating around a table&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      lastMessage: 'John: Meeting moved to 2 PM',
      unreadCount: 0,
      timestamp: new Date(Date.now() - 7200000)
    },
    {
      id: '3',
      name: 'College Friends',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Group of diverse friends laughing together on campus&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      lastMessage: 'Alex: Who\'s coming to the reunion?',
      unreadCount: 12,
      timestamp: new Date(Date.now() - 86400000)
    }
  ]);

  const [chronicles, setChronicles] = useState<Chronicle[]>([
    {
      id: '1',
      author: 'Sarah Johnson',
      content: 'Beautiful sunset at the beach today! 🌅',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Sunset over ocean with vibrant orange and pink sky&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      timestamp: new Date(Date.now() - 10800000),
      isViewed: false
    },
    {
      id: '2',
      author: 'Mike Chen',
      content: 'Just completed my first marathon! 🏃‍♂️',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Runner crossing finish line with arms raised in victory&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      timestamp: new Date(Date.now() - 43200000),
      isViewed: true
    },
    {
      id: '3',
      author: 'Emma Davis',
      content: 'New coffee shop discovery! Best latte ever ☕',
      avatar: 'https://placeholder-image-service.onrender.com/image/64x64?prompt=Artistic latte with heart design in cozy coffee shop&id=f911da43-33b5-4bde-85b7-4e2c12160226',
      timestamp: new Date(Date.now() - 86400000),
      isViewed: false
    }
  ]);

  // Owner information
  const ownerInfo = {
    name: 'Arnold Chirchir',
    email: 'arnoldkipruto193@gmail.com',
    phone: '+254 712 345 678',
    status: 'Available',
    bio: 'Software Developer & Entrepreneur',
    avatar: 'https://placeholder-image-service.onrender.com/image/128x128?prompt=Professional headshot of a software developer with friendly smile&id=f911da43-33b5-4bde-85b7-4e2c12160226'
  };

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    // Mock authentication
    if (email && password) {
      setIsLoggedIn(true);
      setCurrentUser({
        id: 'current',
        name: name || 'Arnold Chirchir',
        email: email,
        avatar: ownerInfo.avatar,
        status: 'online'
      });
    }
  };

  const handleRegister = (e: React.FormEvent) => {
    e.preventDefault();
    // Mock registration
    if (name && email && password) {
      setIsLoggedIn(true);
      setCurrentUser({
        id: 'current',
        name: name,
        email: email,
        avatar: ownerInfo.avatar,
        status: 'online'
      });
    }
  };

  const formatTime = (date: Date) => {
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const minutes = Math.floor(diff / 60000);
    const hours = Math.floor(diff / 3600000);
    const days = Math.floor(diff / 86400000);

    if (minutes < 1) return 'now';
    if (minutes < 60) return `${minutes}m ago`;
    if (hours < 24) return `${hours}h ago`;
    return `${days}d ago`;
  };

  if (!isLoggedIn) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center p-4">
        <Card className="w-full max-w-md">
          <CardHeader>
            <CardTitle className="text-center text-2xl font-bold">
              {isRegistering ? 'Create Account' : 'Welcome Back'}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={isRegistering ? handleRegister : handleLogin} className="space-y-4">
              {isRegistering && (
                <div>
                  <Input
                    type="text"
                    placeholder="Full Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full"
                    required
                  />
                </div>
              )}
              <div>
                <Input
                  type="email"
                  placeholder="Email Address"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full"
                  required
                />
              </div>
              <div>
                <Input
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full"
                  required
                />
              </div>
              <Button type="submit" className="w-full bg-primary text-primary-foreground">
                {isRegistering ? 'Create Account' : 'Sign In'}
              </Button>
            </form>
            <div className="mt-4 text-center">
              <button
                onClick={() => setIsRegistering(!isRegistering)}
                className="text-primary hover:underline"
              >
                {isRegistering ? 'Already have an account? Sign in' : 'Need an account? Sign up'}
              </button>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background flex">
      {/* Sidebar */}
      <div className="w-80 bg-secondary border-r border-border flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-border">
          <div className="flex items-center space-x-3">
            <Avatar>
              <AvatarImage src={currentUser?.avatar} alt="User profile picture" />
              <AvatarFallback>AC</AvatarFallback>
            </Avatar>
            <div className="flex-1">
              <h2 className="font-semibold text-foreground">{currentUser?.name}</h2>
              <p className="text-sm text-muted-foreground">Online</p>
            </div>
          </div>
        </div>

        {/* Search */}
        <div className="p-4 border-b border-border">
          <Input
            placeholder="Search..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full"
          />
        </div>

        {/* Navigation */}
        <div className="flex-1 overflow-y-auto">
          <nav className="space-y-1 p-2">
            <button
              onClick={() => setCurrentView('messages')}
              className={`w-full text-left p-3 rounded-lg transition-colors ${
                currentView === 'messages' 
                  ? 'bg-primary text-primary-foreground' 
                  : 'hover:bg-muted'
              }`}
            >
              Messages
            </button>
            <button
              onClick={() => setCurrentView('groups')}
              className={`w-full text-left p-3 rounded-lg transition-colors ${
                currentView === 'groups' 
                  ? 'bg-primary text-primary-foreground' 
                  : 'hover:bg-muted'
              }`}
            >
              Groups
            </button>
            <button
              onClick={() => setCurrentView('chronicles')}
              className={`w-full text-left p-3 rounded-lg transition-colors ${
                currentView === 'chronicles' 
                  ? 'bg-primary text-primary-foreground' 
                  : 'hover:bg-muted'
              }`}
            >
              Chronicles
            </button>
            <button
              onClick={() => setCurrentView('me')}
              className={`w-full text-left p-3 rounded-lg transition-colors ${
                currentView === 'me' 
                  ? 'bg-primary text-primary-foreground' 
                  : 'hover:bg-muted'
              }`}
            >
              Me
            </button>
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        {/* Content Header */}
        <div className="p-4 border-b border-border">
          <h1 className="text-2xl font-bold text-foreground capitalize">
            {currentView === 'chronicles' ? 'Chronicles' : currentView}
          </h1>
        </div>

        {/* Content Area */}
        <div className="flex-1 overflow-y-auto p-4">
          {currentView === 'messages' && (
            <div className="space-y-4">
              {users.map((user) => (
                <Card key={user.id} className="hover:bg-muted transition-colors cursor-pointer">
                  <CardContent className="p-4">
                    <div className="flex items-center space-x-3">
                      <div className="relative">
                        <Avatar>
                          <AvatarImage src={user.avatar} alt={`Profile picture of ${user.name}`} />
                          <AvatarFallback>{user.name.charAt(0)}</AvatarFallback>
                        </Avatar>
                        <div className={`absolute bottom-0 right-0 w-3 h-3 rounded-full border-2 border-background ${
                          user.status === 'online' ? 'bg-green-500' : 'bg-gray-400'
                        }`} />
                      </div>
                      <div className="flex-1">
                        <div className="flex justify-between items-center">
                          <h3 className="font-semibold text-foreground">{user.name}</h3>
                          <span className="text-sm text-muted-foreground">
                            {formatTime(messages[0].timestamp)}
                          </span>
                        </div>
                        <p className="text-sm text-muted-foreground truncate">
                          {messages.find(m => m.senderId === user.id || m.receiverId === user.id)?.content}
                        </p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          )}

          {currentView === 'groups' && (
            <div className="space-y-4">
              {groups.map((group) => (
                <Card key={group.id} className="hover:bg-muted transition-colors cursor-pointer">
                  <CardContent className="p-4">
                    <div className="flex items-center space-x-3">
                      <Avatar>
                        <AvatarImage src={group.avatar} alt={`Group icon for ${group.name}`} />
                        <AvatarFallback>{group.name.charAt(0)}</AvatarFallback>
                      </Avatar>
                      <div className="flex-1">
                        <div className="flex justify-between items-center">
                          <h3 className="font-semibold text-foreground">{group.name}</h3>
                          {group.unreadCount > 0 && (
                            <span className="bg-primary text-primary-foreground text-xs rounded-full px-2 py-1">
                              {group.unreadCount}
                            </span>
                          )}
                        </div>
                        <p className="text-sm text-muted-foreground truncate">{group.lastMessage}</p>
                        <p className="text-xs text-muted-foreground">{formatTime(group.timestamp)}</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          )}

          {currentView === 'chronicles' && (
            <div className="space-y-4">
              {chronicles.map((chronicle) => (
                <Card key={chronicle.id} className="hover:bg-muted transition-colors">
                  <CardContent className="p-4">
                    <div className="flex items-center space-x-3 mb-3">
                      <Avatar>
                        <AvatarImage src={chronicle.avatar} alt={`Chronicle by ${chronicle.author}`} />
                        <AvatarFallback>{chronicle.author.charAt(0)}</AvatarFallback>
                      </Avatar>
                      <div>
                        <h3 className="font-semibold text-foreground">{chronicle.author}</h3>
                        <p className="text-sm text-muted-foreground">{formatTime(chronicle.timestamp)}</p>
                      </div>
                    </div>
                    <p className="text-foreground">{chronicle.content}</p>
                    {!chronicle.isViewed && (
                      <div className="mt-2 w-2 h-2 bg-primary rounded-full" />
                    )}
                  </CardContent>
                </Card>
              ))}
            </div>
          )}

          {currentView === 'me' && (
            <div className="max-w-md mx-auto space-y-6">
              <Card>
                <CardContent className="p-6">
                  <div className="text-center space-y-4">
                    <Avatar className="w-24 h-24 mx-auto">
                      <AvatarImage src={ownerInfo.avatar} alt="Profile picture of Arnold Chirchir" />
                      <AvatarFallback>AC</AvatarFallback>
                    </Avatar>
                    <div>
                      <h2 className="text-2xl font-bold text-foreground">{ownerInfo.name}</h2>
                      <p className="text-muted-foreground">{ownerInfo.bio}</p>
                    </div>
                  </div>
                  
                  <div className="mt-6 space-y-4">
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Email:</span>
                      <span className="text-foreground">{ownerInfo.email}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Phone:</span>
                      <span className="text-foreground">{ownerInfo.phone}</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-muted-foreground">Status:</span>
                      <span className="text-primary">{ownerInfo.status}</span>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>Account Settings</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <Button variant="outline" className="w-full">Edit Profile</Button>
                  <Button variant="outline" className="w-full">Privacy Settings</Button>
                  <Button variant="outline" className="w-full">Notification Preferences</Button>
                  <Button 
                    variant="destructive" 
                    className="w-full"
                    onClick={() => setIsLoggedIn(false)}
                  >
                    Log Out
                  </Button>
                </CardContent>
              </Card>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
