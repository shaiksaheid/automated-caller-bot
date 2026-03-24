import { LayoutDashboard, Users, Phone, TrendingUp, AlertTriangle, PhoneCall, FileText } from 'lucide-react';


interface SidebarProps {
  activeTab: string;
  onTabChange: (tab: string) => void;
}

export function Sidebar({ activeTab, onTabChange }: SidebarProps) {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'students', label: 'Students', icon: Users },
    { id: 'call-logs', label: 'Call Logs', icon: Phone },
    { id: 'flagged', label: 'Flagged Students', icon: AlertTriangle },
    { id: 'bulk-calls', label: 'Bulk Calls', icon: PhoneCall },
    { id: 'analytics', label: 'Analytics & Reports', icon: TrendingUp },
  ];

  return (
    <div className="w-64 bg-white border-r border-gray-200 h-screen flex flex-col">
      <div className="p-6 border-b border-gray-200">
  <div className="flex items-center gap-3">

    {/* LOGO */}
    <div className="w-15 h-14 rounded-xl bg-gradient-to-br from-blue-100 to-blue-200 border border-blue-300 flex items-center justify-center shadow-sm">
  <img
    src="/cmr_logo.jpg"
    alt="CMR Logo"
    className="w-full h-full object-cover rounded-xl"
  />
</div>

    {/* TEXT */}
    <div className="leading-tight">
      <h1 className="text-lg font-bold text-gray-900">
        CMRTC AutoCaller
      </h1>
      <p className="text-xs text-gray-500">
        Smart Attendance & Alerts
      </p>
    </div>

  </div>
</div>

      <nav className="flex-1 p-4">
        <ul className="space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            
            return (
              <li key={item.id}>
                <button
                  onClick={() => onTabChange(item.id)}
                  className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                    isActive
                      ? 'bg-blue-50 text-blue-700'
                      : 'text-gray-700 hover:bg-gray-50'
                  }`}
                >
                  <Icon className={`w-5 h-5 ${isActive ? 'text-blue-700' : 'text-gray-500'}`} />
                  <span className="font-medium">{item.label}</span>
                </button>
              </li>
            );
          })}
        </ul>
      </nav>

      <div className="p-4 border-t border-gray-200">
        <div className="flex items-center gap-3 px-4 py-3">
          <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center">
            <span className="text-xs font-semibold text-gray-700">AD</span>
          </div>
          <div>
            <p className="text-sm font-medium text-gray-900">Admin User</p>
            <p className="text-xs text-gray-500">admin@college.edu</p>
          </div>
        </div>
      </div>
    </div>
  );
}
