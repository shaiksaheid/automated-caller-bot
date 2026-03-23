export interface Student {
  id: string;
  name: string;
  rollNumber: string;
  class: string;
  department: string;
  parentName: string;
  parentPhone: string;
  email: string;
  isAbsent: boolean;
}

export interface CallLog {
  id: string;
  studentId: string;
  studentName: string;
  parentName: string;
  parentPhone: string;
  callDate: string;
  callTime: string;
  status: 'completed' | 'failed' | 'no-answer' | 'busy';
  duration: number;
  reason: string;
  transcript: string;
  audioUrl: string;
  excuseCategory: string;
}

export interface FlaggedStudent {
  id: string;
  studentId: string;
  studentName: string;
  rollNumber: string;
  repeatedExcuse: string;
  occurrences: number;
  dateRange: string;
  lastOccurrence: string;
  risk: 'high' | 'medium' | 'low';
}

export interface BulkCall {
  id: string;
  campaignName: string;
  totalCalls: number;
  completed: number;
  failed: number;
  createdAt: string;
  status: 'pending' | 'in-progress' | 'completed';
  message: string;
}

export interface Analytics {
  totalCalls: number;
  successRate: number;
  averageDuration: number;
  totalStudents: number;
  absentToday: number;
  flaggedStudents: number;
  commonExcuses: Array<{ excuse: string; count: number }>;
  callTrends: Array<{ date: string; calls: number; success: number }>;
  departmentStats: Array<{ department: string; absent: number; total: number }>;
}
