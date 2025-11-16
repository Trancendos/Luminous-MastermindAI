# AI Orchestration Platform - UI/UX Design Specifications

## Design Philosophy

The AI Orchestration Platform should feel **intelligent, fluid, and empowering**. Users should feel like they're conducting an orchestra of AI agents, not wrestling with complex software.

**Core Design Principles**:
1. **Clarity**: Every action should be obvious and predictable
2. **Speed**: Minimize clicks, maximize efficiency
3. **Intelligence**: The UI should learn and adapt to user behavior
4. **Delight**: Subtle animations and micro-interactions that feel magical
5. **Accessibility**: WCAG 2.1 AA compliance, keyboard navigation, screen reader support

## Color Palette

### Primary Colors
- **Primary**: `#6366F1` (Indigo) - AI intelligence, trust
- **Secondary**: `#8B5CF6` (Purple) - Creativity, innovation
- **Accent**: `#EC4899` (Pink) - Energy, action

### Semantic Colors
- **Success**: `#10B981` (Green)
- **Warning**: `#F59E0B` (Amber)
- **Error**: `#EF4444` (Red)
- **Info**: `#3B82F6` (Blue)

### Neutral Colors
- **Background**: `#0F172A` (Dark slate) - Dark mode primary
- **Surface**: `#1E293B` (Slate 800)
- **Border**: `#334155` (Slate 700)
- **Text Primary**: `#F1F5F9` (Slate 100)
- **Text Secondary**: `#94A3B8` (Slate 400)

### Light Mode (Optional)
- **Background**: `#FFFFFF`
- **Surface**: `#F8FAFC` (Slate 50)
- **Border**: `#E2E8F0` (Slate 200)
- **Text Primary**: `#0F172A`
- **Text Secondary**: `#64748B`

## Typography

### Font Families
- **Headings**: `Inter` (700, 600, 500)
- **Body**: `Inter` (400, 500)
- **Code**: `JetBrains Mono` (400, 500)

### Type Scale
- **H1**: 48px / 3rem (font-bold)
- **H2**: 36px / 2.25rem (font-semibold)
- **H3**: 30px / 1.875rem (font-semibold)
- **H4**: 24px / 1.5rem (font-medium)
- **Body Large**: 18px / 1.125rem
- **Body**: 16px / 1rem
- **Body Small**: 14px / 0.875rem
- **Caption**: 12px / 0.75rem

## Layout System

### Grid
- **Container Max Width**: 1440px
- **Columns**: 12-column grid
- **Gutter**: 24px
- **Margin**: 32px (desktop), 16px (mobile)

### Spacing Scale (Tailwind-based)
- **xs**: 4px (0.25rem)
- **sm**: 8px (0.5rem)
- **md**: 16px (1rem)
- **lg**: 24px (1.5rem)
- **xl**: 32px (2rem)
- **2xl**: 48px (3rem)
- **3xl**: 64px (4rem)

### Breakpoints
- **Mobile**: 0-640px
- **Tablet**: 641-1024px
- **Desktop**: 1025px+

## Component Library

### Navigation

**Top Navigation Bar**:
- Height: 64px
- Background: `surface` with backdrop blur
- Logo: Left-aligned
- Search: Center (expandable)
- User menu: Right-aligned with avatar
- Notifications: Bell icon with badge

**Sidebar Navigation** (Admin/Power Users):
- Width: 280px (expanded), 64px (collapsed)
- Collapsible with toggle button
- Icons + labels
- Active state: Primary color background
- Hover: Subtle background change

### Cards

**Standard Card**:
```css
background: surface
border: 1px solid border
border-radius: 12px
padding: 24px
box-shadow: 0 1px 3px rgba(0,0,0,0.1)
hover: subtle lift (transform: translateY(-2px))
```

**AI Integration Card**:
- Platform logo/icon (48x48)
- Name and status badge
- Last sync time
- Usage stats (tokens, cost)
- Action buttons (Test, Configure, Delete)

**Template Card**:
- Avatar/icon
- Name and description
- Rating stars
- Usage count
- Price (if marketplace)
- Quick actions (Use, Edit, Share)

### Buttons

**Primary Button**:
```css
background: primary
color: white
padding: 12px 24px
border-radius: 8px
font-weight: 500
hover: darken 10%
active: scale(0.98)
disabled: opacity 50%
```

**Secondary Button**:
```css
background: transparent
border: 1px solid border
color: text-primary
hover: background surface
```

**Icon Button**:
```css
size: 40x40
border-radius: 8px
hover: background surface
```

### Form Inputs

**Text Input**:
```css
height: 44px
padding: 12px 16px
border: 1px solid border
border-radius: 8px
background: surface
focus: border primary, ring 3px primary/20%
```

**Textarea**:
- Min height: 120px
- Auto-resize based on content
- Max height: 400px with scroll

**Select Dropdown**:
- Custom styled (not native)
- Search functionality for long lists
- Keyboard navigation

**Toggle Switch**:
- Width: 44px, Height: 24px
- Smooth animation (300ms)
- Clear on/off states

### Chat Interface

**Message Bubble (User)**:
```css
background: primary
color: white
border-radius: 16px 16px 4px 16px
padding: 12px 16px
max-width: 70%
align: right
```

**Message Bubble (AI)**:
```css
background: surface
color: text-primary
border: 1px solid border
border-radius: 16px 16px 16px 4px
padding: 12px 16px
max-width: 70%
align: left
avatar: AI icon/logo (32x32)
```

**Multi-AI Response**:
- Side-by-side layout (desktop)
- Stacked layout (mobile)
- Clear AI attribution
- Voting buttons (thumbs up/down)

**Streaming Indicator**:
- Animated typing dots
- Pulse effect on AI avatar
- Smooth text reveal

### Modals & Dialogs

**Modal Overlay**:
```css
background: rgba(0,0,0,0.5)
backdrop-filter: blur(4px)
```

**Modal Content**:
```css
background: surface
border-radius: 16px
max-width: 600px
padding: 32px
box-shadow: 0 20px 25px rgba(0,0,0,0.3)
```

**Dialog Actions**:
- Right-aligned
- Primary action on right
- Cancel/secondary on left

### Data Visualization

**Usage Chart**:
- Line chart for token usage over time
- Bar chart for cost by AI platform
- Pie chart for request distribution
- Color-coded by AI platform

**Terminology Graph**:
- Force-directed graph
- Nodes: terminology entries
- Edges: relationships
- Interactive (zoom, pan, click)
- Hover: show definition

### Loading States

**Skeleton Loader**:
- Animated gradient shimmer
- Match component dimensions
- Smooth transition to real content

**Spinner**:
- Size: 24px (small), 40px (medium), 64px (large)
- Color: primary
- Smooth rotation animation

**Progress Bar**:
- Height: 4px
- Indeterminate: sliding animation
- Determinate: fill percentage

### Empty States

**No Data**:
- Illustration or icon
- Helpful message
- Call-to-action button
- Example: "No AI integrations yet. Connect your first AI to get started."

### Notifications & Toasts

**Toast Notification**:
```css
position: fixed
bottom: 24px
right: 24px
background: surface
border: 1px solid border
border-radius: 12px
padding: 16px
box-shadow: 0 4px 6px rgba(0,0,0,0.1)
max-width: 400px
auto-dismiss: 5 seconds
```

**Types**:
- Success: Green accent
- Error: Red accent
- Warning: Amber accent
- Info: Blue accent

## Page Layouts

### Dashboard (Home)
```
┌─────────────────────────────────────┐
│  Top Nav                            │
├──────┬──────────────────────────────┤
│      │  Welcome Header              │
│      ├──────────────────────────────┤
│ Side │  Quick Stats (4 cards)       │
│ Nav  ├──────────────────────────────┤
│      │  Recent Conversations        │
│      ├──────────────────────────────┤
│      │  Active Workflows            │
└──────┴──────────────────────────────┘
```

### AI Integrations
```
┌─────────────────────────────────────┐
│  Top Nav                            │
├──────┬──────────────────────────────┤
│      │  Page Header + Add Button    │
│      ├──────────────────────────────┤
│ Side │  Integration Cards (Grid)    │
│ Nav  │  ┌──────┐ ┌──────┐ ┌──────┐│
│      │  │OpenAI│ │Claude│ │Gemini││
│      │  └──────┘ └──────┘ └──────┘│
└──────┴──────────────────────────────┘
```

### Terminology Dictionary
```
┌─────────────────────────────────────┐
│  Top Nav                            │
├──────┬──────────────────────────────┤
│      │  Search Bar + Add Button     │
│      ├──────────────────────────────┤
│ Side │  ┌─────────┬────────────────┐│
│ Nav  │  │ List    │ Detail View    ││
│      │  │ (Left)  │ (Right)        ││
│      │  │         │                ││
│      │  └─────────┴────────────────┘│
└──────┴──────────────────────────────┘
```

### Chat Interface
```
┌─────────────────────────────────────┐
│  Top Nav                            │
├──────┬──────────────────────────────┤
│ Conv │  Chat Header (AI selection) │
│ List ├──────────────────────────────┤
│      │  Message Area (scrollable)  │
│      │                              │
│      ├──────────────────────────────┤
│      │  Input Box + Send Button    │
└──────┴──────────────────────────────┘
```

### Template Builder
```
┌─────────────────────────────────────┐
│  Top Nav                            │
├──────┬──────────────────────────────┤
│      │  Template Name + Save Button │
│      ├──────────────────────────────┤
│ Side │  ┌──────────┬──────────────┐│
│ Nav  │  │ Config   │ Preview      ││
│      │  │ (Left)   │ (Right)      ││
│      │  │          │              ││
│      │  └──────────┴──────────────┘│
└──────┴──────────────────────────────┘
```

## Micro-Interactions

### Hover Effects
- **Cards**: Subtle lift (2px) + shadow increase
- **Buttons**: Background color shift
- **Links**: Underline slide-in animation
- **Icons**: Scale up 110%

### Click Feedback
- **Buttons**: Scale down 98% on active
- **Cards**: Brief highlight flash
- **Checkboxes**: Checkmark slide-in

### Loading Animations
- **Skeleton**: Left-to-right shimmer
- **Spinner**: Smooth rotation
- **Progress**: Smooth fill animation

### Success Animations
- **Checkmark**: Draw animation
- **Confetti**: Particle burst (for major actions)
- **Pulse**: Brief scale pulse

## Accessibility

### Keyboard Navigation
- Tab order: logical flow
- Focus indicators: 2px primary ring
- Shortcuts: Cmd/Ctrl + K (search), Cmd/Ctrl + / (help)

### Screen Readers
- Semantic HTML (nav, main, article, aside)
- ARIA labels for icon buttons
- Live regions for dynamic content
- Skip to main content link

### Color Contrast
- Text on background: 4.5:1 minimum
- Large text: 3:1 minimum
- Interactive elements: 3:1 minimum

## Mobile Responsive Design

### Mobile Navigation
- Bottom tab bar (5 main sections)
- Hamburger menu for secondary nav
- Swipe gestures for navigation

### Mobile Chat
- Full-screen chat interface
- Floating action button for new chat
- Swipe to delete conversations

### Mobile Forms
- Large touch targets (44x44 minimum)
- Native input types (email, tel, etc.)
- Auto-focus on first field

## Dark Mode (Default)

The platform defaults to dark mode with optional light mode toggle.

**Dark Mode Benefits**:
- Reduced eye strain for long sessions
- Better for low-light environments
- Modern, professional aesthetic
- Lower power consumption (OLED screens)

## Animation Timing

- **Fast**: 150ms (hover, focus)
- **Medium**: 300ms (transitions, modals)
- **Slow**: 500ms (page transitions, complex animations)
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)` (ease-in-out)

## Performance Guidelines

- **First Contentful Paint**: < 1.5s
- **Time to Interactive**: < 3.5s
- **Cumulative Layout Shift**: < 0.1
- **Largest Contentful Paint**: < 2.5s

## Design System Tools

- **Component Library**: shadcn/ui (Tailwind-based)
- **Icons**: Lucide React
- **Charts**: Recharts or Chart.js
- **Animations**: Framer Motion
- **Drag & Drop**: dnd-kit
