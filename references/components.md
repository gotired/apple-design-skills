# Components — HIG rules, condensed

Every rule below is a condensed "best practice" heading from the Apple Human Interface
Guidelines page for that component. Rules are cross-platform; platform-specific deltas
live in `platforms.md`. Full page: `https://developer.apple.com/design/human-interface-guidelines/<slug>`.

Use this file two ways:
- **Building** — read the section for the component you are about to build.
- **Reviewing** — read the section and check the UI against each line.


## Content

### Charts
Organize data in a chart to communicate information with clarity and visual appeal.
- Choose a mark type based on the information you want to communicate about the data
- Consider combining mark types when it adds clarity to your chart
- Use a fixed or dynamic axis range depending on the meaning of your chart
- Define the value of the lower bound based on mark type and chart usage
- Prefer familiar sequences of values in the tick and grid-line labels for an axis
- Tailor the appearance of grid lines and labels to a chart’s use cases
- Write descriptions that help people understand what a chart does before they view it
- Summarize the main message of your chart to help make it approachable and useful for everyone
- Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements
- In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart
- Make every chart in your app accessible
- Let people interact with the data when it makes sense, but don’t require interaction to reveal critical information
- Make it easy for everyone to interact with a chart
- Make an interactive chart easy to navigate when using keyboard commands (including full keyboard access) or Switch Control
- Help people notice important changes in a chart
- Align a chart with surrounding interface elements
- Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart
- Aid comprehension by adding visual separation between contiguous areas of color
- Consider using Audio Graphs to give VoiceOver users more information about your chart
- Write accessibility labels that support the purpose of your chart
- Prioritize clarity and comprehensiveness
- Avoid using subjective terms
- Maximize clarity in data descriptions by avoiding potentially ambiguous formats and abbreviations
- Describe what the chart’s details represent, not what they look like
- Be consistent throughout your app when referring to a specific axis
- Hide visible text labels for axes and ticks from assistive technologies

### Image views
An image view displays a single image — or in some cases, an animated sequence of images — on a transparent or opaque background.
- Use an image view when the primary purpose of the view is simply to display an image
- If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view
- Take care when overlaying text on images
- Aim to use a consistent size for all images in an animated sequence

### Text views
A text view displays multiline, styled text content, which can optionally be editable.
- Use a text view when you need to display text that’s long, editable, or in a special format
- Make useful text selectable

### Web views
A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.
- Support forward and back navigation when appropriate
- Avoid using a web view to build a web browser


## Layout and organization

### Boxes
A box creates a visually distinct group of logically related information and components.
- Prefer keeping a box relatively small in comparison with its containing view
- Consider using padding and alignment to communicate additional grouping within a box
- Provide a succinct introductory title if it helps clarify the box’s contents
- If you need a title, write a brief phrase that describes the contents

### Collections
A collection manages an ordered set of content and presents it in a customizable and highly visual layout.
- Use the standard row or grid layout whenever possible
- Consider using a table instead of a collection for text
- Make it easy to choose an item
- Add custom interactions when necessary
- Consider using animations to provide feedback when people insert, delete, or reorder items

### Column views
A column view — also called a **browser** — lets people view and navigate a data hierarchy using a series of vertical columns.
- Show the root level of your data hierarchy in the first column
- Consider showing information about the selected item when there are no nested items to display
- Let people resize columns

### Disclosure controls
Disclosure controls reveal and hide information and functionality related to specific controls or views.
- Use a disclosure control to hide details until they’re relevant
- Provide a descriptive label when using a disclosure triangle
- Place a disclosure button near the content that it shows and hides
- Use no more than one disclosure button in a single view

### Labels
A label is a static piece of text that people can read and often copy, but not edit.
- Use a label to display a small amount of text that people don’t need to edit
- Prefer system fonts
- Use system-provided label colors to communicate relative importance
- Make useful label text selectable

### Lists and tables
Lists and tables present data in one or more columns of rows.
- Prefer displaying text in a list or table
- Let people edit a table when it makes sense
- Provide appropriate feedback when people select a list item
- Keep item text succinct so row content is comfortable to read
- Consider ways to preserve readability of text that might otherwise get clipped or truncated
- Use descriptive column headings in a multicolumn table
- Choose a table or list style that coordinates with your data and platform
- Choose a row style that fits the information you need to display

### Lockups
Lockups combine multiple separate views into a single, interactive unit.
- Allow adequate space between lockups
- Use consistent lockup sizes within a row or group
- Prefer images over initials

### Outline views
An outline view presents hierarchical data in a scrolling list of cells that are organized into columns and rows.
- Use a table instead of an outline view to present data that’s not hierarchical
- Expose data hierarchy in the first column only
- Use descriptive column headings to provide context
- Consider letting people click column headings to sort an outline view
- Let people resize columns
- Make it easy for people to expand or collapse nested containers
- Retain people’s expansion choices
- Consider using alternating row colors in multi-column outline views
- Let people edit data if it makes sense in your app
- Consider using a centered ellipsis to truncate cell text instead of clipping it
- Consider offering a search field to help people find values quickly in a lengthy outline view

### Split views
A split view manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, collections, images, and custom views.
- To support navigation, persistently highlight the current selection in each pane that leads to the detail view
- Consider letting people drag and drop content between panes

### Tab views
A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.
- Use a tab view to present closely related areas of content
- Make sure the controls within a pane affect content only in the same pane
- Provide a label for each tab that describes the contents of its pane
- Avoid using a pop-up button to switch between tabs
- Avoid providing more than six tabs in a tab view
- In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view


## Menus and actions

### Activity views
An activity view — often called a **share sheet** — presents a range of tasks that people can perform in the current context.
- Avoid creating duplicate versions of common actions that are already available in the activity view
- Consider using a symbol to represent your custom activity
- Write a succinct, descriptive title for each custom action you provide
- Make sure activities are appropriate for the current context
- Use the Share button to display an activity view
- If necessary, create a custom interface that feels familiar to people
- Streamline and limit interaction
- Avoid placing a modal view above your extension
- If necessary, provide an image that communicates the purpose of your extension
- Use your main app to denote the progress of a lengthy operation

### Buttons
A button initiates an instantaneous action.
- Style: A visual style based on size, color, and shape.
- Content: A symbol (or icon), text label, or both that a button displays to convey its purpose.
- Role: A system-defined role that identifies a button’s semantic meaning and can affect its appearance.
- Make buttons easy for people to use
- Always include a press state for a custom button
- In general, use a button that has a prominent visual style for the most likely action in a view
- Use style — not size — to visually distinguish the preferred choice among multiple options
- Avoid applying a similar color to button labels and content layer backgrounds
- Ensure that each button clearly communicates its purpose
- Try to associate familiar actions with familiar icons
- Consider using text when a short label communicates more clearly than an icon
- Normal: No specific meaning.
- Primary: The button is the default button — the button people are most likely to choose.
- Cancel: The button cancels the current action.
- Destructive: The button performs an action that can result in data destruction.
- Assign the primary role to the button people are most likely to choose
- Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice

### Context menus
A context menu provides access to functionality that’s directly related to an item, without cluttering the interface.
- Prioritize relevancy when choosing items to include in a context menu
- Aim for a small number of menu items
- Support context menus consistently throughout your app
- Always make context menu items available in the main interface, too
- If you need to use submenus to manage a menu’s complexity, keep them to one level
- Hide unavailable menu items, don’t dim them
- Aim to place the most frequently used menu items where people are likely to encounter them first
- Show keyboard shortcuts in your app’s main menus, not in context menus
- Follow best practices for using separators
- In iOS, iPadOS, and visionOS, warn people about context menu items that can destroy data
- Include a title in a context menu only if doing so clarifies the menu’s effect
- Represent menu item actions with familiar icons

### Dock menus
On a Mac, people can secondary click an app’s or game’s icon in the Dock to reveal a Dock menu, which presents both system-provided and custom items.
- Make custom Dock menu items available in other places, too
- Prefer high-value custom items for your Dock menu

### Edit menus
An edit menu lets people make changes to selected content in the current view, in addition to offering related commands like Copy, Select, Translate, and Look Up.
- Prefer the system-provided edit menu
- Let people reveal an edit menu using the system-defined interactions they already know
- Offer commands that are relevant in the current context, removing or dimming commands that don’t apply
- List custom commands near relevant system-provided ones
- When it makes sense, let people select and copy noneditable text
- Support undo and redo when possible
- In general, avoid implementing other controls that perform the same functions as edit menu items
- Differentiate different types of deletion commands when necessary
- Create short labels for custom commands

### Home Screen quick actions
Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.
- Create quick actions for compelling, high-value tasks
- Avoid making unpredictable changes to quick actions
- For each quick action, provide a succinct title that instantly communicates the results of the action
- Provide a familiar interface icon for each quick action
- Don’t use an emoji in place of a symbol or interface icon

### Menus
A menu reveals its options when people interact with it, making it a space-efficient way to present commands in your app or game.
- For each menu item, write a label that clearly and succinctly describes it
- To be consistent with platform experiences, use title-style capitalization
- Remove articles like
- Show people when a menu item is unavailable
- Append an ellipsis to a menu item’s label when the action requires more information before it can complete
- Represent common actions consistently
- Use menu item icons sparingly and with purpose
- Apply a uniform visual treatment across menu items in the same group
- Prefer listing important or frequently used menu items first
- Consider grouping logically related items
- Prefer keeping all logically related commands in the same group, even if the commands don’t all have the same importance
- Be mindful of menu length
- Use submenus sparingly
- Limit the depth and length of submenus
- Make sure a submenu remains available even when its nested menu items are unavailable
- Prefer using a submenu to indenting menu items
- Consider using a changeable label that describes an item’s current state
- Include a verb if a changeable label isn’t clear enough
- If necessary, display both menu items instead of one toggled item
- Consider using a checkmark to show that an attribute is currently in effect
- Consider offering a menu item that makes it easy to remove multiple toggled attributes
- Let players navigate in-game menus using the platform’s default interaction method
- Make sure your menus remain easy to open and read on all platforms you support

### Ornaments
In visionOS, an ornament presents controls and information related to a window, without crowding or obscuring the window’s contents.
- Consider using an ornament to present frequently needed controls or information in a consistent location that doesn’t clutter the window
- In general, keep an ornament visible
- If you need to display multiple ornaments, prioritize the overall visual balance of the window
- Aim to keep an ornament’s width the same or narrower than the width of the associated window
- Consider using borderless buttons in an ornament
- Use system-provided toolbars and tab bars unless you need to create custom components

### Pop-up buttons
A pop-up button displays a menu of mutually exclusive options.
- Use a pop-up button to present a flat list of mutually exclusive options or states
- Provide a useful default selection
- Give people a way to predict a pop-up button’s options without opening it
- Consider using a pop-up button when space is limited and you don’t need to display all options all the time
- If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations

### Pull-down buttons
A pull-down button displays a menu of items or actions that directly relate to the button’s purpose.
- Use a pull-down button to present commands or items that are directly related to the button’s action
- Avoid putting all of a view’s actions in one pull-down button
- Balance menu length with ease of use
- Display a succinct menu title only if it adds meaning
- Let people know when a pull-down button’s menu item is destructive, and ask them to confirm their intent
- Include an interface icon with a menu item when it provides value

### The menu bar
On a Mac or an iPad, the menu bar at the top of the screen displays the top-level menus in your app or game.
- YourAppName: (you supply a short version of your app’s name for this menu’s title)
- Support the default system-defined menus and their ordering
- Always show the same set of menu items
- Represent menu item actions with familiar icons
- Support the keyboard shortcuts defined for the standard menu items you include
- Prefer short, one-word menu titles
- Display the About menu item first
- Determine whether Find menu items belong in the Edit menu
- Provide a View menu even if your app supports only a subset of the standard view functions
- Ensure that each show/hide item title reflects the current state of the corresponding view
- Provide app-specific menus for custom commands
- As much as possible, reflect your app’s hierarchy in app-specific menus
- Aim to list app-specific menus in order from most to least general or commonly used
- Provide a Window menu even if your app has only one window
- Consider including menu items for showing and hiding panels
- Avoid making a dynamic menu item the only way to accomplish a task
- Use dynamic menu items primarily in menu bar menus
- Require only a single modifier key to reveal a dynamic menu item

### Toolbars
A toolbar provides convenient access to frequently used commands, controls, navigation, and search.
- Choose items deliberately to avoid overcrowding
- Add a More menu to contain additional actions
- In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items
- Reduce the use of toolbar backgrounds and tinted controls
- Avoid applying a similar color to toolbar item labels and content layer backgrounds
- Prefer using standard components in a toolbar
- Consider temporarily hiding toolbars for a distraction-free experience
- Provide a useful title for each window
- Don’t title windows with your app name
- Write a concise title
- Use the standard Back and Close buttons
- Provide actions that support the main tasks people perform
- Make sure the meaning of each control is clear
- Prefer system-provided symbols without borders
- Use the `.prominent` style for key actions such as Done or Submit
- Leading edge: Elements that let people return to the previous document and show or hide a sidebar appear at the far leading edge, followed by the view title. Next to the titl
- Center area: Common, useful controls appear in the center area, and the view title can appear here if it’s not on the leading edge. In macOS and iPadOS, people can add, remo
- Trailing edge: The trailing edge contains important items that need to remain available, buttons that open nearby inspectors, an optional search field, and the More menu that
- Group toolbar items logically by function and frequency of use
- Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections
- Keep consistent groupings and placement across platforms
- Minimize the number of groups
- Keep actions with text labels separate


## Navigation and search

### Path controls
A path control shows the file system path of a selected file or folder.
- Use a path control in the window body, not the window frame

### Search fields
A search field lets people search a collection of content for specific terms they enter.
- Use placeholder text to help people know what they can search for
- If possible, start search immediately when a person types
- Consider showing suggested search terms
- Simplify search results
- Consider letting people filter search results
- Use a scope bar to filter among clearly defined search categories
- Default to a broader scope and let people refine it as they need
- Use tokens to filter by common search terms or items
- Consider pairing tokens with search suggestions

### Sidebars
A sidebar appears on the leading side of a view and lets people navigate between areas of your app or top-level collections of content, like folders and playlists.
- Extend visually rich content beneath the sidebar
- When possible, let people customize the contents of a sidebar
- Group hierarchy with disclosure controls if your app has a lot of content
- Consider using familiar symbols to represent items in the sidebar
- Consider letting people hide the sidebar
- In general, show no more than two levels of hierarchy in a sidebar
- If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group
- Make sure any sidebar icon colors you choose serve a clear purpose

### Tab bars
A tab bar lets people navigate between top-level sections of your app.
- Use a tab bar to support navigation, not to provide actions
- Make sure the tab bar is visible when people navigate to different sections of your app
- Use the appropriate number of tabs required to help people navigate your app
- Avoid overflow tabs
- Don’t disable or hide tab bar buttons, even when their content is unavailable
- Include tab labels to help with navigation
- Consider using SF Symbols to provide familiar, scalable tab bar icons
- Use a badge to indicate that critical information is available
- Avoid applying a similar color to tab labels and content layer backgrounds

### Token fields
A token field is a type of text field that can convert text into **tokens** that are easy to select and manipulate.
- Add value with a context menu
- Consider providing additional ways to convert text into tokens
- Consider customizing the delay the system uses before showing suggested tokens


## Presentation

### Action sheets
An action sheet is a modal view that presents choices related to an action people initiate.
- Use an action sheet — not an alert — to offer choices related to an intentional action
- Use action sheets sparingly
- Aim to keep titles short enough to display on a single line
- Provide a message only if necessary
- If necessary, provide a Cancel button that lets people reject an action that might destroy data
- Make destructive choices visually prominent

### Alerts
An alert gives people critical information they need right away.
- Use alerts sparingly
- Avoid using an alert merely to provide information
- Avoid displaying alerts for common, undoable actions, even when they’re destructive
- Avoid showing an alert when your app starts
- In all alert copy, be direct, and use a neutral, approachable tone
- Write a title that clearly and succinctly describes the situation
- Include informative text only if it adds value
- Avoid explaining alert buttons
- If supported, include a text field only if you need people’s input to resolve the situation
- Create succinct, logical button titles
- Avoid using OK as the default button title unless the alert is purely informational
- Place buttons where people expect
- Use the destructive style to identify a button that performs a destructive action people didn’t deliberately choose
- If there’s a destructive action, include a Cancel button to give people a clear, safe way to avoid the action
- Provide alternative ways to cancel an alert when it makes sense

### Page controls
A page control displays a row of indicator images, each of which represents a page in a flat list.
- Use page controls to represent movement between an ordered list of pages
- Center a page control at the bottom of the view or window
- Although page controls can handle any number of pages, don’t display too many
- Make sure custom indicator images are simple and clear
- Customize the default indicator image only when it enhances the page control’s overall meaning
- Avoid using more than two different indicator images in a page control
- Avoid coloring indicator images

### Panels
In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection.
- Use a panel to give people quick access to important controls or information related to the content they’re working with
- Consider using a panel to present inspector functionality
- Prefer simple adjustment controls in a panel
- Write a brief title that describes the panel’s purpose
- Show and hide panels appropriately
- Avoid including panels in the Window menu’s documents list
- In general, avoid making a panel’s minimize button available
- Refer to panels by title in your interface and in help documentation
- Prefer standard panels
- Maintain one panel style when your app switches modes
- Use color sparingly in HUDs

### Popovers
A popover is a transient view that appears above other content when people click or tap a control or interactive area.
- Use a popover to expose a small amount of information or functionality
- Consider using popovers when you want more room for content
- Position popovers appropriately
- Use a Close button for confirmation and guidance only
- Always save work when automatically closing a nonmodal popover
- Show one popover at a time
- Don’t show another view over a popover
- When possible, let people close one popover and open another with a single click or tap
- Avoid making a popover too big
- Provide a smooth transition when changing the size of a popover
- Avoid using the word
- Avoid using a popover to show a warning

### Scroll views
A scroll view lets people view content that’s larger than the view’s boundaries by moving the content vertically or horizontally.
- Support default scrolling gestures and keyboard shortcuts
- Make it apparent when content is scrollable
- Avoid putting a scroll view inside another scroll view with the same orientation
- Consider supporting page-by-page scrolling if it makes sense for your content
- In some cases, scroll automatically to help people find their place
- If you support zoom, set appropriate maximum and minimum scale values
- Prefer the automatic scroll edge effect style
- Only use a scroll edge effect when a scroll view is behind floating interface elements
- Apply one scroll edge effect per view

### Sheets
A sheet helps people perform a scoped task that’s closely related to their current context.
- For complex or prolonged user flows, consider alternatives to sheets
- Display only one sheet at a time from the main interface
- Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view
- Provide an alternative to the Done button

### Windows
A window presents UI views and components in your app or game.
- Make sure that your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows
- Choose the right moment to open a new window
- Consider providing the option to view content in a new window
- Avoid creating custom window UI


## Selection and input

### Color wells
A color well lets people adjust the color of text, shapes, guides, and other onscreen elements.
- Consider the system-provided color picker for a familiar experience

### Combo boxes
A combo box combines a text field with a pull-down button in a single control.
- Populate the field with a meaningful default value from the list
- Use an introductory label to let people know what types of items to expect
- Provide relevant choices
- Make sure list items aren’t wider than the text field

### Digit entry views
A digit entry view fills the entire screen and prompts people to enter a series of digits, like a PIN, using a digit-specific keyboard.
- Use secure digit fields
- Clearly state the purpose of the digit entry view

### Image wells
An image well is an editable version of an image view.
- Revert to a default image when necessary
- If your image well supports copy and paste, make sure the standard copy and paste menu items are available

### Pickers
A picker displays one or more scrollable lists of distinct values that people can choose from.
- Consider using a picker to offer medium-to-long lists of items
- Use predictable and logically ordered values
- Avoid switching views to show a picker
- Consider providing less granularity when specifying minutes in a date picker

### Segmented controls
A segmented control is a linear set of two or more segments, each of which functions as a button.
- Use a segmented control to provide closely related choices that affect an object, state, or view
- Consider a segmented control when it’s important to group functions together, or to clearly show their selection state
- Keep control types consistent within a single segmented control
- Limit the number of segments in a control
- In general, keep segment size consistent
- Prefer using either text or images — not a mix of both — in a single segmented control
- As much as possible, use content with a similar size in each segment
- Use nouns or noun phrases for segment labels

### Sliders
A slider is a horizontal track with a control, called a thumb, that people can adjust between a minimum and maximum value.
- Customize a slider’s appearance if it adds value
- Use familiar slider directions
- Consider supplementing a slider with a corresponding text field and stepper

### Steppers
A stepper is a two-segment control that people use to increase or decrease an incremental value.
- Make the value that a stepper affects obvious
- Consider pairing a stepper with a text field when large value changes are likely

### Text fields
A text field is a rectangular area in which people enter or edit small, specific pieces of text.
- Use a text field to request a small amount of information, such as a name or an email address
- Show a hint in a text field to help communicate its purpose
- Use secure text fields to hide private data
- To the extent possible, match the size of a text field to the quantity of anticipated text
- Evenly space multiple text fields
- Ensure that tabbing between multiple fields flows as people expect
- Validate fields when it makes sense
- Use a number formatter to help with numeric data
- Adjust line breaks according to the needs of the field
- Consider using an expansion tooltip to show the full version of clipped or truncated text
- In iOS, iPadOS, tvOS, and visionOS apps, show the appropriate keyboard type
- Minimize text entry in your tvOS and watchOS apps

### Toggles
A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.
- Use a toggle to help people choose between two opposing values that affect the state of content or a view
- Clearly identify the setting, view, or content the toggle affects
- Make sure the visual differences in a toggle’s state are obvious

### Virtual keyboards
On devices without physical keyboards, the system offers various types of virtual keyboards people can use to enter data.
- Choose a keyboard that matches the type of content people are editing
- [tab] ASCII capable
- [tab] ASCII capable number pad
- [tab] Email address
- [tab] Name phone pad
- [tab] Numbers and punctuation
- Consider customizing the Return key type if it helps clarify the text-entry experience
- Make sure your custom input view makes sense in the context of your app
- Play the standard keyboard sound while people type
- Provide an obvious and easy way to switch between keyboards
- Avoid duplicating system-provided keyboard features
- Consider providing a keyboard tutorial in your app


## Status

### Activity rings
Activity rings show an individual’s daily progress toward Move, Exercise, and Stand goals.
- Display Activity rings when they’re relevant to the purpose of your app
- Use Activity rings only to show Move, Exercise, and Stand information
- Use Activity rings to show progress for a single person
- Always keep the visual appearance of Activity rings the same, regardless of where you display them
- To display a label or value that’s directly associated with an Activity ring, use the colors that match it
- Maintain Activity ring margins
- Differentiate other ring-like elements from Activity rings
- Don’t send notifications that repeat the same information the Activity app sends
- Don’t use Activity rings for decoration
- Don’t use Activity rings for branding

### Gauges
A gauge displays a specific numerical value within a range of values.
- Write succinct labels that describe the current value and both endpoints of the range
- Consider filling the path with a gradient to help communicate the purpose of the gauge

### Progress indicators
Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.
- Determinate: , for a task with a well-defined duration, such as a file conversion
- Indeterminate: , for unquantifiable tasks, such as loading or synchronizing complex data
- When possible, use a determinate progress indicator
- Be as accurate as possible when reporting advancement in a determinate progress indicator
- Keep progress indicators moving so people know something is continuing to happen
- When possible, switch a progress bar from indeterminate to determinate
- Don’t switch from the circular style to the bar style
- If it’s helpful, display a description that provides additional context for the task
- Display a progress indicator in a consistent location
- When it’s feasible, let people halt processing
- Let people know when halting a process has a negative consequence

### Rating indicators
A rating indicator uses a series of horizontally arranged graphical symbols — by default, stars — to communicate a ranking level.
- Make it easy to change rankings
- If you replace the star with a custom symbol, make sure that its purpose is clear


## System experiences

### App Shortcuts
An App Shortcut gives people access to your app’s key functions or content throughout the system.
- To surface common types of app functionality throughout the system, consider adopting app schemas instead
- Offer App Shortcuts for your app’s most common and important tasks
- Add flexibility by letting people choose from a set of options
- Ask for clarification in response to a request that’s missing optional information
- Keep voice interactions simple
- Make App Shortcuts discoverable in your app
- Provide enough detail for interaction on audio-only devices
- Provide brief, memorable activation phrases and natural variants
- When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that
- When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase

### Complications
A complication displays timely, relevant information on the watch face, where people can view it each time they raise their wrist.
- Identify essential, dynamic content that people want to view at a glance
- Support all complication families when possible
- Consider creating multiple complications for each family
- Define a different deep link for each complication you support
- Keep privacy in mind
- Carefully consider when to update data
- Choose a ring or gauge style based on the data you need to display
- Make sure images look good in tinted mode
- Recognize that people might prefer to use tinted mode for complications, instead of viewing them in full color
- When creating complication content, generally use line widths of two points or greater
- Provide a set of static placeholder images for each complication you support

### Controls
A control provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.
- Offer controls for actions that provide the most benefit without having to launch your app
- Update controls when someone interacts with them, when an action completes, or remotely with a push notification
- Choose a descriptive symbol that suggests the behavior of the control
- Use symbol animations to highlight state changes
- Select a tint color that works with your app’s brand
- Help people provide additional information the system needs to perform an action
- Provide hint text for the Action button
- If your control title or value can vary, include a placeholder
- Hide sensitive information when the device is locked
- Require authentication for actions that affect security
- Use the same camera UI in your app and your camera experience
- Provide instructions for adding the control

### Live Activities
A Live Activity lets people track the progress of an activity, event, or task at a glance.
- Offer Live Activities for tasks and events that have a defined beginning and end
- Focus on important information that people need to see at a glance
- Don’t use a Live Activity to display ads or promotions
- Avoid displaying sensitive information
- Create a Live Activity that matches your app’s visual aesthetic and personality in both dark and light appearances
- If you include a logo mark, display it without a container
- Don’t add elements to your app that draw attention to the Dynamic Island
- Ensure text is easy to read
- Adapt to different screen sizes and presentations
- Adjust element size and placement for efficient use of space
- Use familiar layouts for custom views and layouts
- Use consistent margins and concentric placement
- When separating a block of content, place it in an inset container shape or use a thick line
- Dynamically change the height of your Live Activity on the Lock Screen or in the expanded presentation
- Carefully consider using a custom background color and opacity
- Use color to express the character and identity of your app
- Tint your Live Activity’s key line color so that it matches your content
- Use animations to reinforce the information you’re communicating and to bring attention to updates
- Animate layout changes
- Try to avoid overlapping elements
- Make sure tapping the Live Activity opens your app at the right location
- Focus on simple, direct actions
- Consider letting people respond to event or progress updates
- Start Live Activities at appropriate times, and make it easy for people to turn them off in your app
- Offer an App Shortcut that starts your Live Activity
- Update a Live Activity only when new content is available
- Alert people only for essential updates that require their attention
- Let people track multiple events efficiently with a single Live Activity
- Always end a Live Activity immediately when the task or event ends, and consider setting a custom dismissal time
- Start with the iPhone design, then refine it for other contexts
- Focus on the most important information
- Ensure unified information and design of the compact presentations in the Dynamic Island
- Keep content as narrow as possible and ensure it’s snug against the TrueDepth camera
- Link to relevant app content
- Ensure that your Live Activity is recognizable in the minimal presentation
- Maintain the relative placement of elements to create a coherent layout between presentations
- Wrap content tightly around the TrueDepth camera
- Don’t replicate notification layouts
- Choose colors that work well on a personalized Lock Screen
- Make sure your design, assets, and colors look great and offer enough contrast in Dark Mode and on an Always-On display
- Verify the generated color of the dismiss button
- Use standard margins to align your design with notifications
- Update your layout for StandBy
- Consider using the default background color in StandBy
- Use standard margins and avoid extending graphic elements to the edge of the screen
- Verify your design in Night Mode
- Consider creating a custom layout if your Live Activity would benefit from larger text or additional information
- Carefully consider including buttons or toggles in your custom layout

### Notifications
A notification gives people timely, high-value information they can understand at a glance.
- Provide concise, informative notifications
- Avoid sending multiple notifications for the same thing, even if someone hasn’t responded
- Avoid sending a notification that tells people to perform specific tasks within your app
- Use an alert — not a notification — to display an error message
- Handle notifications gracefully when your app is in the foreground
- Avoid including sensitive, personal, or confidential information in a notification
- Create a short title if it provides context for the notification content
- Write succinct, easy-to-read notification content
- Provide generically descriptive text to display when notification previews aren’t available
- Avoid including your app name or icon
- Consider providing a sound to supplement your notifications
- Provide beneficial actions that make sense in the context of your notification
- Avoid providing an action that merely opens your app
- Prefer nondestructive actions
- Provide a simple, recognizable interface icon for each notification action
- Use a badge only to show people how many unread notifications they have
- Make sure badging isn’t the only method you use to communicate essential information
- Keep badges up to date
- Avoid creating a custom image or component that mimics the appearance or behavior of a badge

### Snippets
When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation.
- Dialogue: The app intent dialogue that Siri speaks to communicate the snippet’s information. The system includes the dialogue text by default and places it above the cust
- Custom view: A view that visually communicates the snippet’s information. A custom view can include one or more buttons for modifying the content of the snippet, getting mor
- System-provided button(s)
- Keep content concise
- Choose a descriptive label for a confirmation snippet’s primary button
- Communicate a snippet’s purpose visually

### Status bars
A status bar appears along the upper edge of the screen and displays information about the device’s current state, like the time, cellular carrier, and battery level.
- Obscure content under the status bar
- Consider temporarily hiding the status bar when displaying full-screen media
- Avoid permanently hiding the status bar

### Top Shelf
The Apple TV Home Screen provides an area called Top Shelf, which showcases your content in a rich, engaging way while also giving people access to their favorite apps in the Dock.
- Help people jump right into your content
- Feature new content
- Personalize people’s favorite content
- Avoid showing advertisements or prices
- Showcase compelling dynamic content that can help draw people in and encourage them to view more
- If you don’t provide the recommended full-screen content, supply at least one static image as a fallback
- Avoid implying interactivity in a static image
- Provide a title that identifies the currently playing content
- Provide enough content to constitute a complete row
- Be aware of additional scaling when combining image sizes
- Provide three to eight images
- If you need text, add it to your image

### Watch faces
A watch face is a view that people choose as their primary view in watchOS.
- Help people discover your app by sharing watch faces that feature your complications
- Display a preview of each watch face you share
- Aim to offer shareable watch faces for all Apple Watch devices
- Respond gracefully if people choose an incompatible watch face

### Widgets
A widget provides quick access to essential information and focused interactions from your app or game in additional contexts.
- [tab] Extra large portrait
- [tab] Accessory circular
- [tab] Accessory corner
- [tab] Accessory inline
- [tab] Accessory rectangular
- [tab] iPhone Lock Screen
- [tab] Watch complication
- [tab] Smart Stack on Apple Watch
- Choose simple ideas that relate to your app’s main purpose
- Aim to create a widget that gives people quick access to the content they want
- Prefer dynamic information that changes throughout the day
- Look for opportunities to surprise and delight
- Offer widgets in multiple sizes when doing so adds value
- Balance information density
- Display only the information that’s directly related to the widget’s main purpose
- Use brand elements thoughtfully
- Choose between automatically displaying content and letting people customize displayed information
- Avoid mirroring your widget’s appearance within your app
- Let people know when authentication adds value
- Keep your widget up to date
- Use system functionality to refresh dates and times in your widget
- Use animated transitions to bring attention to data updates
- Offer simple, relevant functionality and reserve complexity for your app
- Ensure that a widget interaction opens your app at the right location
- Offer interactivity while remaining glanceable and uncluttered
- In general, use standard margins to ensure legibility
- Coordinate the corner radius of your content with the corner radius of the widget
- Prefer using the system font, text styles, and SF Symbols
- Avoid very small font sizes
- Avoid rasterizing text
- Use color to enhance a widget’s appearance without competing with its content
- Convey meaning without relying on specific colors to represent information
- Use full-color images judiciously
- Support light and dark appearances
- Group widget components into an accented and a primary group
- Offer enough contrast to ensure legibility
- Create optimized assets for the best vibrant effect
- Design a realistic preview to display in the widget gallery
- Design placeholder content that helps people recognize your widget
- Write a succinct widget description
- Group your widget’s sizes together, and provide a single description
- Consider coloring the Add button
