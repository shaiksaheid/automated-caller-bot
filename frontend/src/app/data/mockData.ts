import { Student, CallLog, FlaggedStudent, BulkCall, Analytics } from '@/app/types';

export const mockStudents: Student[] = [
  {
    id: '1',
    name: 'Rahul Sharma',
    rollNumber: 'CS2024001',
    class: 'Second Year',
    department: 'Computer Science',
    parentName: 'Mr. Vijay Sharma',
    parentPhone: '+91-9876543210',
    email: 'rahul.sharma@college.edu',
    isAbsent: false
  },
  {
    id: '2',
    name: 'Priya Patel',
    rollNumber: 'EC2024015',
    class: 'Third Year',
    department: 'Electronics',
    parentName: 'Mrs. Anjali Patel',
    parentPhone: '+91-9876543211',
    email: 'priya.patel@college.edu',
    isAbsent: true
  },
  {
    id: '3',
    name: 'Amit Kumar',
    rollNumber: 'ME2024032',
    class: 'First Year',
    department: 'Mechanical',
    parentName: 'Mr. Rajesh Kumar',
    parentPhone: '+91-9876543212',
    email: 'amit.kumar@college.edu',
    isAbsent: true
  },
  {
    id: '4',
    name: 'Sneha Reddy',
    rollNumber: 'CS2024007',
    class: 'Second Year',
    department: 'Computer Science',
    parentName: 'Dr. Krishna Reddy',
    parentPhone: '+91-9876543213',
    email: 'sneha.reddy@college.edu',
    isAbsent: false
  },
  {
    id: '5',
    name: 'Arjun Singh',
    rollNumber: 'CE2024021',
    class: 'Fourth Year',
    department: 'Civil',
    parentName: 'Mr. Harpal Singh',
    parentPhone: '+91-9876543214',
    email: 'arjun.singh@college.edu',
    isAbsent: true
  },
  {
    id: '6',
    name: 'Ananya Gupta',
    rollNumber: 'EC2024018',
    class: 'Third Year',
    department: 'Electronics',
    parentName: 'Mrs. Meera Gupta',
    parentPhone: '+91-9876543215',
    email: 'ananya.gupta@college.edu',
    isAbsent: false
  },
  {
    id: '7',
    name: 'Rohan Verma',
    rollNumber: 'CS2024012',
    class: 'Second Year',
    department: 'Computer Science',
    parentName: 'Mr. Ashok Verma',
    parentPhone: '+91-9876543216',
    email: 'rohan.verma@college.edu',
    isAbsent: false
  },
  {
    id: '8',
    name: 'Kavya Nair',
    rollNumber: 'ME2024045',
    class: 'First Year',
    department: 'Mechanical',
    parentName: 'Mr. Suresh Nair',
    parentPhone: '+91-9876543217',
    email: 'kavya.nair@college.edu',
    isAbsent: true
  }
];

export const mockCallLogs: CallLog[] = [
  {
    id: 'call-1',
    studentId: '2',
    studentName: 'Priya Patel',
    parentName: 'Mrs. Anjali Patel',
    parentPhone: '+91-9876543211',
    callDate: '2026-01-29',
    callTime: '09:15 AM',
    status: 'completed',
    duration: 45,
    reason: 'Medical',
    transcript: 'My daughter is not feeling well. She has fever and headache. I took her to the doctor this morning.',
    audioUrl: 'mock-audio-1.mp3',
    excuseCategory: 'Medical'
  },
  {
    id: 'call-2',
    studentId: '3',
    studentName: 'Amit Kumar',
    parentName: 'Mr. Rajesh Kumar',
    parentPhone: '+91-9876543212',
    callDate: '2026-01-29',
    callTime: '09:20 AM',
    status: 'completed',
    duration: 38,
    reason: 'Family Emergency',
    transcript: 'There was a family emergency. We had to visit our relative in the hospital urgently.',
    audioUrl: 'mock-audio-2.mp3',
    excuseCategory: 'Family Emergency'
  },
  {
    id: 'call-3',
    studentId: '5',
    studentName: 'Arjun Singh',
    parentName: 'Mr. Harpal Singh',
    parentPhone: '+91-9876543214',
    callDate: '2026-01-29',
    callTime: '09:25 AM',
    status: 'no-answer',
    duration: 0,
    reason: 'N/A',
    transcript: '',
    audioUrl: '',
    excuseCategory: 'No Response'
  },
  {
    id: 'call-4',
    studentId: '8',
    studentName: 'Kavya Nair',
    parentName: 'Mr. Suresh Nair',
    parentPhone: '+91-9876543217',
    callDate: '2026-01-29',
    callTime: '09:30 AM',
    status: 'completed',
    duration: 42,
    reason: 'Medical',
    transcript: 'She has stomach pain and vomiting since last night. Doctor advised rest for today.',
    audioUrl: 'mock-audio-3.mp3',
    excuseCategory: 'Medical'
  },
  {
    id: 'call-5',
    studentId: '2',
    studentName: 'Priya Patel',
    parentName: 'Mrs. Anjali Patel',
    parentPhone: '+91-9876543211',
    callDate: '2026-01-26',
    callTime: '10:05 AM',
    status: 'completed',
    duration: 40,
    reason: 'Medical',
    transcript: 'She is having fever and cold. Not feeling well enough to attend classes.',
    audioUrl: 'mock-audio-4.mp3',
    excuseCategory: 'Medical'
  },
  {
    id: 'call-6',
    studentId: '3',
    studentName: 'Amit Kumar',
    parentName: 'Mr. Rajesh Kumar',
    parentPhone: '+91-9876543212',
    callDate: '2026-01-22',
    callTime: '09:40 AM',
    status: 'completed',
    duration: 35,
    reason: 'Family Emergency',
    transcript: 'Family function that we had to attend. It was important and unavoidable.',
    audioUrl: 'mock-audio-5.mp3',
    excuseCategory: 'Family Emergency'
  }
];

export const mockFlaggedStudents: FlaggedStudent[] = [
  {
    id: 'flag-1',
    studentId: '2',
    studentName: 'Priya Patel',
    rollNumber: 'EC2024015',
    repeatedExcuse: 'Medical - Fever/Cold',
    occurrences: 4,
    dateRange: 'Jan 10 - Jan 29, 2026',
    lastOccurrence: '2026-01-29',
    risk: 'high'
  },
  {
    id: 'flag-2',
    studentId: '3',
    studentName: 'Amit Kumar',
    rollNumber: 'ME2024032',
    repeatedExcuse: 'Family Emergency',
    occurrences: 3,
    dateRange: 'Jan 15 - Jan 29, 2026',
    lastOccurrence: '2026-01-29',
    risk: 'medium'
  }
];

export const mockBulkCalls: BulkCall[] = [
  {
    id: 'bulk-1',
    campaignName: 'Annual Day Invitation',
    totalCalls: 150,
    completed: 150,
    failed: 0,
    createdAt: '2026-01-20',
    status: 'completed',
    message: 'Dear parents, we invite you to our college annual day celebration on February 5th, 2026.'
  },
  {
    id: 'bulk-2',
    campaignName: 'Exam Schedule Notification',
    totalCalls: 200,
    completed: 185,
    failed: 15,
    createdAt: '2026-01-25',
    status: 'completed',
    message: 'The final semester examinations will commence from March 1st, 2026. Please check the website for detailed schedule.'
  },
  {
    id: 'bulk-3',
    campaignName: 'Fee Reminder',
    totalCalls: 75,
    completed: 45,
    failed: 5,
    createdAt: '2026-01-29',
    status: 'in-progress',
    message: 'This is a reminder that the semester fee payment deadline is February 10th, 2026.'
  }
];

export const mockAnalytics: Analytics = {
  totalCalls: 347,
  successRate: 87.5,
  averageDuration: 41,
  totalStudents: 1250,
  absentToday: 4,
  flaggedStudents: 2,
  commonExcuses: [
    { excuse: 'Medical', count: 125 },
    { excuse: 'Family Emergency', count: 78 },
    { excuse: 'Transportation Issues', count: 45 },
    { excuse: 'Personal Reasons', count: 32 },
    { excuse: 'No Response', count: 67 }
  ],
  callTrends: [
    { date: '2026-01-23', calls: 12, success: 10 },
    { date: '2026-01-24', calls: 8, success: 7 },
    { date: '2026-01-25', calls: 15, success: 13 },
    { date: '2026-01-26', calls: 10, success: 9 },
    { date: '2026-01-27', calls: 6, success: 5 },
    { date: '2026-01-28', calls: 14, success: 12 },
    { date: '2026-01-29', calls: 4, success: 3 }
  ],
  departmentStats: [
    { department: 'Computer Science', absent: 2, total: 320 },
    { department: 'Electronics', absent: 1, total: 280 },
    { department: 'Mechanical', absent: 2, total: 250 },
    { department: 'Civil', absent: 1, total: 200 },
    { department: 'Electrical', absent: 0, total: 200 }
  ]
};
