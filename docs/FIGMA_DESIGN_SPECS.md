# Luminous-MastermindAI - Figma Design Specifications

## Overview
Comprehensive design specifications for creating the Figma prototype of the AI Orchestration Platform.

---

## Figma File Structure

```
Luminous-MastermindAI/
├── 📄 Cover Page
├── 🎨 Design System
│   ├── Colors
│   ├── Typography
│   ├── Components
│   ├── Icons
│   └── Spacing
├── 📱 Wireframes
│   ├── Desktop
│   ├── Tablet
│   └── Mobile
├── 🎯 High-Fidelity Mockups
│   ├── Dashboard
│   ├── AI Dictionary
│   ├── Integrations Hub
│   ├── Template Builder
│   ├── Multi-AI Chat
│   ├── Analytics
│   └── Settings
├── 🔄 User Flows
│   ├── Onboarding
│   ├── Create AI Agent
│   ├── Add Integration
│   └── Multi-AI Conversation
└── 🚀 Prototype
    ├── Desktop Prototype
    └── Mobile Prototype
```

---

## Design System Setup

### 1. Color Styles

#### Primary Palette
```
Primary/500    #3B82F6    RGB(59, 130, 246)
Primary/600    #2563EB    RGB(37, 99, 235)
Primary/700    #1D4ED8    RGB(29, 78, 216)

Secondary/500  #8B5CF6    RGB(139, 92, 246)
Secondary/600  #7C3AED    RGB(124, 58, 237)
Secondary/700  #6D28D9    RGB(109, 40, 217)

Accent/500     #10B981    RGB(16, 185, 129)
Accent/600     #059669    RGB(5, 150, 105)
Accent/700     #047857    RGB(4, 120, 87)
```

#### Semantic Colors
```
Success/500    #10B981    RGB(16, 185, 129)
Warning/500    #F59E0B    RGB(245, 158, 11)
Error/500      #EF4444    RGB(239, 68, 68)
Info/500       #3B82F6    RGB(59, 130, 246)
```

#### Neutral Palette (Dark Theme)
```
Slate/900      #0F172A    RGB(15, 23, 42)     Background
Slate/800      #1E293B    RGB(30, 41, 59)     Surface
Slate/700      #334155    RGB(51, 65, 85)     Border
Slate/600      #475569    RGB(71, 85, 105)    Disabled
Slate/400      #94A3B8    RGB(148, 163, 184)  Text Secondary
Slate/100      #F1F5F9    RGB(241, 245, 249)  Text Primary
```

### 2. Typography Styles

#### Font Setup
- **Primary Font**: Inter (Google Fonts)
- **Monospace Font**: JetBrains Mono (Google Fonts)

#### Text Styles
```
Heading 1
  Font: Inter Bold
  Size: 36px
  Line Height: 44px
  Letter Spacing: -0.02em

Heading 2
  Font: Inter Semibold
  Size: 30px
  Line Height: 38px
  Letter Spacing: -0.01em

Heading 3
  Font: Inter Semibold
  Size: 24px
  Line Height: 32px
  Letter Spacing: 0

Body Large
  Font: Inter Regular
  Size: 18px
  Line Height: 28px
  Letter Spacing: 0

Body
  Font: Inter Regular
  Size: 16px
  Line Height: 24px
  Letter Spacing: 0

Body Small
  Font: Inter Regular
  Size: 14px
  Line Height: 20px
  Letter Spacing: 0

Caption
  Font: Inter Medium
  Size: 12px
  Line Height: 16px
  Letter Spacing: 0.01em

Code
  Font: JetBrains Mono Regular
  Size: 14px
  Line Height: 20px
  Letter Spacing: 0
```

### 3. Spacing System

```
Space/4     4px      0.25rem
Space/8     8px      0.5rem
Space/12    12px     0.75rem
Space/16    16px     1rem
Space/20    20px     1.25rem
Space/24    24px     1.5rem
Space/32    32px     2rem
Space/40    40px     2.5rem
Space/48    48px     3rem
Space/64    64px     4rem
Space/80    80px     5rem
```

### 4. Border Radius

```
Radius/SM   4px      Small elements (tags, badges)
Radius/MD   8px      Cards, buttons
Radius/LG   12px     Modals, panels
Radius/XL   16px     Large containers
Radius/Full 9999px   Pills, avatars
```

### 5. Shadows

```
Shadow/SM
  0 1px 2px 0 rgba(0, 0, 0, 0.05)

Shadow/MD
  0 4px 6px -1px rgba(0, 0, 0, 0.1),
  0 2px 4px -1px rgba(0, 0, 0, 0.06)

Shadow/LG
  0 10px 15px -3px rgba(0, 0, 0, 0.1),
  0 4px 6px -2px rgba(0, 0, 0, 0.05)

Shadow/XL
  0 20px 25px -5px rgba(0, 0, 0, 0.1),
  0 10px 10px -5px rgba(0, 0, 0, 0.04)

Shadow/Glow
  0 0 20px rgba(59, 130, 246, 0.3)
```

---

## Component Library

### 1. Buttons

#### Primary Button
```
Size: 40px height
Padding: 12px 24px
Background: Primary/500
Text: Slate/100
Border Radius: Radius/MD
Font: Body Small (Semibold)
Hover: Primary/600
Active: Primary/700
Disabled: Slate/600 (opacity 50%)
```

#### Secondary Button
```
Size: 40px height
Padding: 12px 24px
Background: Transparent
Border: 1px solid Slate/700
Text: Slate/100
Border Radius: Radius/MD
Font: Body Small (Semibold)
Hover: Slate/800
Active: Slate/700
```

#### Icon Button
```
Size: 40px × 40px
Background: Transparent
Icon: 20px
Border Radius: Radius/MD
Hover: Slate/800
Active: Slate/700
```

### 2. Input Fields

#### Text Input
```
Height: 40px
Padding: 10px 12px
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/MD
Text: Body Small
Placeholder: Slate/400
Focus: Border Primary/500, Shadow/Glow
Error: Border Error/500
```

#### Search Input
```
Height: 40px
Padding: 10px 12px 10px 40px
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/MD
Icon: Search (left, 16px)
Text: Body Small
Placeholder: Slate/400
```

#### Textarea
```
Min Height: 120px
Padding: 12px
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/MD
Text: Body Small
Resize: Vertical
```

### 3. Cards

#### Standard Card
```
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/LG
Padding: 24px
Shadow: Shadow/SM
Hover: Shadow/MD
```

#### Metric Card
```
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/LG
Padding: 20px
Min Height: 120px
Layout: Vertical stack
  - Label (Caption, Slate/400)
  - Value (Heading 2, Slate/100)
  - Change indicator (Body Small, Success/500 or Error/500)
```

#### Integration Card
```
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/LG
Padding: 20px
Layout:
  - Header (Icon + Name + Status badge)
  - Content (API key, usage stats)
  - Actions (Configure, Test buttons)
```

### 4. Navigation

#### Sidebar Navigation
```
Width: 280px
Background: Slate/900
Border Right: 1px solid Slate/700
Padding: 24px 16px

Nav Item:
  Height: 40px
  Padding: 8px 12px
  Border Radius: Radius/MD
  Icon: 20px
  Text: Body Small
  Hover: Slate/800
  Active: Primary/500 (background), Slate/100 (text)
```

#### Top Navigation
```
Height: 64px
Background: Slate/900
Border Bottom: 1px solid Slate/700
Padding: 0 24px
Layout: Flex (space-between)
  - Left: Logo + Title
  - Right: Profile + Settings
```

### 5. Modals & Dialogs

#### Modal Container
```
Max Width: 600px
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/XL
Shadow: Shadow/XL
Padding: 32px

Layout:
  - Header (Heading 3 + Close button)
  - Content (Body text + form fields)
  - Footer (Cancel + Confirm buttons)
```

#### Toast Notification
```
Width: 360px
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/LG
Shadow: Shadow/LG
Padding: 16px
Position: Top-right, stacked

Layout:
  - Icon (20px, colored by type)
  - Content (Title + Message)
  - Close button
```

### 6. Status Indicators

#### Badge
```
Height: 24px
Padding: 4px 8px
Border Radius: Radius/Full
Font: Caption (Semibold)

Connected: Background Success/500, Text Slate/100
Disconnected: Background Slate/700, Text Slate/400
Warning: Background Warning/500, Text Slate/900
Error: Background Error/500, Text Slate/100
```

#### Status Dot
```
Size: 8px
Border Radius: Radius/Full

Connected: Background Success/500
Disconnected: Background Slate/600
Warning: Background Warning/500
Error: Background Error/500
```

### 7. Data Visualization

#### Progress Bar
```
Height: 8px
Background: Slate/700
Border Radius: Radius/Full

Fill:
  Background: Primary/500
  Border Radius: Radius/Full
  Animated: Smooth transition
```

#### Chart Container
```
Background: Slate/800
Border: 1px solid Slate/700
Border Radius: Radius/LG
Padding: 24px

Chart Colors:
  - Primary: Primary/500
  - Secondary: Secondary/500
  - Accent: Accent/500
  - Grid: Slate/700
  - Labels: Slate/400
```

---

## Page Layouts

### 1. Dashboard Layout

```
┌──────────────────────────────────────────────────┐
│ Top Navigation (64px)                            │
├──────────┬───────────────────────────────────────┤
│          │                                       │
│ Sidebar  │ Main Content Area                     │
│ (280px)  │ - Padding: 32px                       │
│          │ - Max Width: 1440px                   │
│          │ - Centered                            │
│          │                                       │
│          │ Grid Layout:                          │
│          │ - 3 columns on desktop                │
│          │ - 2 columns on tablet                 │
│          │ - 1 column on mobile                  │
│          │ - Gap: 24px                           │
│          │                                       │
└──────────┴───────────────────────────────────────┘
```

### 2. Full-Width Layout (Chat, Analytics)

```
┌──────────────────────────────────────────────────┐
│ Top Navigation (64px)                            │
├──────────────────────────────────────────────────┤
│                                                  │
│ Main Content Area (Full Width)                   │
│ - Padding: 32px                                  │
│ - Max Width: 1920px                              │
│ - Centered                                       │
│                                                  │
│ Content:                                         │
│ - Chat interface or charts                       │
│ - Flexible height                                │
│ - Scrollable                                     │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 3. Split View Layout (Template Builder)

```
┌──────────────────────────────────────────────────┐
│ Top Navigation (64px)                            │
├──────────┬───────────────────────────────────────┤
│          │                                       │
│ Config   │ Preview Area                          │
│ Panel    │ - Live preview of AI agent            │
│ (400px)  │ - Test chat interface                 │
│          │ - Real-time updates                   │
│ Forms &  │                                       │
│ Controls │                                       │
│          │                                       │
└──────────┴───────────────────────────────────────┘
```

---

## Interaction States

### 1. Hover States
- **Buttons**: Background darkens, shadow increases
- **Cards**: Shadow increases, border brightens
- **Links**: Underline appears, color brightens
- **Nav Items**: Background appears

### 2. Active States
- **Buttons**: Background darkens further, shadow decreases
- **Nav Items**: Background Primary/500, text white
- **Inputs**: Border Primary/500, glow shadow

### 3. Disabled States
- **Buttons**: Opacity 50%, cursor not-allowed
- **Inputs**: Background Slate/900, border Slate/700
- **Text**: Color Slate/600

### 4. Loading States
- **Skeleton**: Animated gradient (Slate/800 to Slate/700)
- **Spinner**: Rotating circle (Primary/500)
- **Progress**: Animated bar

### 5. Error States
- **Input**: Border Error/500, helper text Error/500
- **Card**: Border Error/500, icon Error/500
- **Toast**: Background Error/500, icon white

---

## Animation Guidelines

### 1. Transitions
```
Duration: 200ms (fast), 300ms (normal), 500ms (slow)
Easing: cubic-bezier(0.4, 0, 0.2, 1)

Use cases:
- Fast: Hover states, button clicks
- Normal: Modal open/close, page transitions
- Slow: Complex animations, data visualization
```

### 2. Micro-interactions
- **Button Click**: Scale down to 0.95, bounce back
- **Toast Appear**: Slide in from right, fade in
- **Modal Open**: Fade in background, scale up modal
- **Loading**: Pulse animation, rotating spinner

### 3. Page Transitions
- **Fade**: Opacity 0 to 1 (300ms)
- **Slide**: Transform translateX (300ms)
- **Scale**: Transform scale 0.95 to 1 (300ms)

---

## Responsive Breakpoints

```
Mobile:     < 640px
Tablet:     640px - 1024px
Desktop:    1024px - 1440px
Large:      > 1440px
```

### Responsive Behavior

#### Desktop (> 1024px)
- Full sidebar visible
- 3-column grid for cards
- Full-width charts
- Expanded nav items with labels

#### Tablet (640px - 1024px)
- Collapsible sidebar
- 2-column grid for cards
- Responsive charts
- Icon-only nav with tooltips

#### Mobile (< 640px)
- Hidden sidebar (hamburger menu)
- 1-column grid for cards
- Stacked charts
- Bottom navigation bar

---

## Accessibility Specifications

### 1. Color Contrast
- **Text on Background**: Minimum 7:1 (AAA)
- **UI Elements**: Minimum 3:1 (AA)
- **Focus Indicators**: Minimum 3:1 (AA)

### 2. Focus States
```
Outline: 2px solid Primary/500
Offset: 2px
Border Radius: Radius/MD
```

### 3. Keyboard Navigation
- **Tab Order**: Logical, left-to-right, top-to-bottom
- **Skip Links**: "Skip to main content"
- **Shortcuts**: Clearly labeled, documented

### 4. Screen Reader Support
- **Alt Text**: All images and icons
- **ARIA Labels**: Interactive elements
- **Live Regions**: Dynamic content updates

---

## Icon System

### Icon Library: Lucide React

#### Common Icons
```
Home:           Home
Dashboard:      LayoutDashboard
Dictionary:     Book
Integrations:   Plug
Template:       Layers
Chat:           MessageSquare
Analytics:      BarChart3
Settings:       Settings
Profile:        User
Notification:   Bell
Search:         Search
Add:            Plus
Edit:           Pencil
Delete:         Trash2
Export:         Download
Import:         Upload
Close:          X
Check:          Check
Alert:          AlertTriangle
Info:           Info
AI Agent:       Bot
Connected:      CheckCircle
Disconnected:   XCircle
Loading:        Loader2
```

#### Icon Sizes
```
Small:    16px
Medium:   20px
Large:    24px
XLarge:   32px
```

---

## Figma Plugins Recommended

1. **Iconify**: Access Lucide icons directly
2. **Contrast**: Check color contrast ratios
3. **Stark**: Accessibility testing
4. **Autoflow**: Create user flow diagrams
5. **Content Reel**: Generate realistic content
6. **Unsplash**: High-quality placeholder images

---

## Prototype Specifications

### 1. Interactions to Include

#### Dashboard
- Click metric cards → Navigate to detailed view
- Click integration card → Open configuration modal
- Click "Add New" → Open creation flow

#### AI Dictionary
- Search terms → Filter results
- Click term card → Expand details
- Click "Export to AI" → Show success toast

#### Integrations Hub
- Click "Connect" → Show OAuth flow
- Click "Test" → Show loading, then success/error
- Toggle switches → Update status

#### Template Builder
- Drag sliders → Update preview
- Toggle checkboxes → Enable/disable features
- Click "Test Agent" → Open chat simulation

#### Multi-AI Chat
- Type message → Show typing indicator
- Send message → Show AI responses sequentially
- Click action button → Navigate to integration

### 2. Prototype Flow

```
Start Screen: Dashboard
  ↓
User clicks "Create AI Agent"
  ↓
Template Builder opens
  ↓
User configures agent
  ↓
User clicks "Test Agent"
  ↓
Chat simulation opens
  ↓
User sends test message
  ↓
AI responds
  ↓
User clicks "Deploy"
  ↓
Success toast appears
  ↓
Return to Dashboard (agent now visible)
```

---

## Export Specifications

### 1. Design Handoff
- **Format**: Figma Dev Mode
- **Assets**: Export at 1x, 2x, 3x
- **Code**: CSS, Tailwind classes
- **Measurements**: Spacing, sizing values

### 2. Asset Export

#### Icons
- Format: SVG
- Naming: icon-name.svg
- Color: Current color (for CSS control)

#### Images
- Format: WebP (with PNG fallback)
- Optimization: TinyPNG
- Naming: descriptive-name.webp

#### Illustrations
- Format: SVG
- Optimization: SVGO
- Naming: illustration-name.svg

---

## Design Checklist

### Before Development Handoff

- [ ] All pages designed at 3 breakpoints
- [ ] All interactive states defined
- [ ] All components documented
- [ ] Color contrast checked (AAA)
- [ ] Typography hierarchy clear
- [ ] Spacing system consistent
- [ ] Icon system complete
- [ ] Prototype tested with users
- [ ] Accessibility reviewed
- [ ] Design tokens exported
- [ ] Assets optimized and exported
- [ ] Developer documentation written

---

## Next Steps

1. **Create Figma File**: Set up with this structure
2. **Build Component Library**: Create all reusable components
3. **Design High-Fidelity Mockups**: Apply design system
4. **Create Prototype**: Link screens with interactions
5. **User Testing**: Validate with target users
6. **Iterate**: Refine based on feedback
7. **Developer Handoff**: Export assets and documentation

---

*These specifications follow the foundational principles of zero-cost, modular design, and compliance-first architecture as specified in the Luminous-MastermindAI framework.*
