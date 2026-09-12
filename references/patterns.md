# Patterns — HIG rules, condensed

Patterns are whole-flow rules: onboarding, feedback, loading, modality, search, settings,
data entry, notifications. Condensed from the Apple Human Interface Guidelines.
Full page: `https://developer.apple.com/design/human-interface-guidelines/<slug>`.


## Charting data
Presenting data in a chart can help you communicate information with clarity and appeal.
- Use a chart when you want to highlight important information about a dataset
- Keep a chart simple, letting people choose when they want additional details
- Make every chart in your app accessible
- In general, prefer using common chart types
- If you need to create a chart that presents data in a novel way, help people learn how to interpret the chart
- Examine the data from multiple levels or perspectives to find details you can display to enhance the chart
- Aid comprehension by adding descriptive text to the chart
- Match the size of a chart to its functionality, topic, and level of detail
- Prefer consistency across multiple charts, deviating only when you need to highlight differences
- Maintain continuity among multiple charts that use the same data

## Collaboration and sharing
Great collaboration and sharing experiences are simple and responsive, letting people engage with the content while communicating effectively with others.
- Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating
- If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports
- Write succinct phrases that summarize the sharing permissions you support
- Provide a set of simple sharing options that streamline collaboration setup
- Prominently display the Collaboration button as soon as collaboration starts
- Provide custom actions in the collaboration popover only if needed
- If it makes sense in your app, customize the title of the modal view’s collaboration-management button
- Consider posting collaboration event notifications in Messages

## Drag and drop
Using drag and drop, people can move or duplicate selected photos, text, and other content by dragging the selection from one location to another.
- As much as possible, support drag and drop throughout your app
- Offer alternative ways to accomplish drag-and-drop actions
- Determine when dragging and dropping content within your app results in a move or a copy
- Support multi-item drag and drop when it makes sense
- Prefer letting people undo a drag-and-drop operation
- Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity
- Consider supporting spring loading
- Display a drag image as soon as people drag a selection about three points
- If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation
- Show people whether a destination can accept dragged content
- When people drop an item on an invalid destination, or when dropping fails, provide visual feedback
- Scroll the contents of a destination when necessary
- When there’s a choice, pick the richest version of dropped content your app can accept
- Extract only the relevant portion of dropped content if necessary
- When a physical keyboard is attached, check for the Option key at drop time
- Provide feedback when dropped content needs time to transfer
- Provide feedback when dropped content initiates a task or action
- Apply appropriate styling to dropped text
- After a drop, maintain the content’s selection state in the destination, updating it in the source as needed

## Entering data
When you need information from people, design ways that make it easy for them to provide it without making mistakes.
- Get information from the system whenever possible
- Be clear about the data you need
- Use a secure text-entry field when appropriate
- Never prepopulate a password field
- When possible, offer choices instead of requiring text entry
- As much as possible, let people provide data by dragging and dropping it or by pasting it
- Dynamically validate field values
- When data entry is necessary, make sure people understand that they must provide the required data before they can proceed

## Feedback
Feedback helps people know what’s happening, discover what they can do next, understand the results of actions, and avoid mistakes.
- Make sure all feedback is accessible
- Consider integrating status feedback into your interface
- Use alerts to deliver critical — and ideally actionable — information
- Warn people when they initiate a task that can cause data loss that’s unexpected and irreversible
- When it makes sense, confirm that a significant action or task has completed
- Show people when a command can’t be carried out and help them understand why

## File management
Some apps can support documents and files that people expect to manage throughout the system.
- Use app menus and keyboard shortcuts to give people convenient ways to create and open documents
- If your app requires a custom file browser, support people’s understanding of the platform’s file system
- Help people be confident that their work is always preserved unless they cancel or delete it
- Hide file extensions by default, but let people view them if they choose
- Use a Quick Look viewer to let people preview a file even when your app can’t open it
- Consider implementing a Quick Look generator if your app produces custom file types

## Going full screen
iPhone, iPad, and Mac offer full-screen modes that let people expand a window to fill the screen, hiding system controls and providing a distraction-free environment.
- Support full-screen mode when it makes sense for your experience
- If necessary, adjust your layout in full-screen mode, but don’t programmatically resize your window
- Continue to provide access to essential features and controls so people can complete their task without exiting full-screen mode
- Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode
- After people switch away from your full-screen experience, help them resume where they left off when they return
- Let people choose when to exit full-screen mode
- Prioritize content by temporarily hiding toolbars and navigation controls

## Launching
A streamlined launch experience helps people start using your app or game immediately.
- If the platform requires it, provide a launch screen
- If you need a splash screen, consider displaying it at the beginning of your onboarding flow
- Restore the previous state when your app restarts so people can continue where they left off
- Not applicable for macOS, visionOS, or watchOS
- Downplay the launch experience
- Design a launch screen that’s nearly identical to the first screen of your app or game
- Avoid including text on your launch screen, even if your first screen displays text

## Live-viewing apps
As you design a live-viewing app, prioritize the content and create fun, fluid interactions that encourage immersion in the live-viewing experience.
- Feature live content prominently and make it easy to access
- Let people tap once — or not at all — to start playback
- Make sure live content looks live
- Consider indicating the progress of currently playing live content
- Give people additional actions and viewing alternatives
- Consider using a content footer for browsing channels during playback
- Provide instant visual feedback when people change channels
- Match audio to the current context
- Prominently display current information and make it easy to return to playback
- Make browsing the EPG effortless
- Group content into familiar categories to help people find it more easily
- Let people browse the EPG without leaving their current content
- Let people start and stop recording from the info panel
- Let people record a future program in a view that provides details about the content
- Help people adapt the recording experience to their needs
- Allow playback and other content-specific actions within your cloud DVR area
- Consider offering a control that lets people manage cloud DVR settings

## Loading
The best content-loading experience finishes before people become aware of it.
- Show something as soon as possible
- Let people do other things in your app or game while they wait for content to load
- If loading takes an unavoidably long time, give people something interesting to view while they wait
- Improve installation and launch time by downloading large assets in the background
- Clearly communicate that content is loading and how long it might take to complete
- For games, consider creating a custom loading view

## Managing accounts
When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.
- Explain the benefits of creating an account and how to sign up
- Delay sign-in for as long as possible
- If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey
- Always identify the authentication method you offer
- Refer only to authentication methods that are available in the current context
- In general, avoid offering an app-specific setting for opting in to biometric authentication
- Avoid using the term
- Provide a clear way to initiate account deletion within your app or game
- Provide a consistent account-deletion experience whether people perform it within your app or game or on the website
- Consider letting people schedule account deletion to occur in the future
- Tell people when account deletion will complete, and notify them when it’s finished
- If you support in-app purchases, help people understand how billing and cancellation work when they delete their account
- Avoid displaying a sign-out option when people are signed in at the system level
- Never instruct people to sign out by adjusting privacy controls

## Managing notifications
Notifications can give people timely and important information, whether the device is locked or in use.
- Passive: . Information people can view at their leisure, like a restaurant recommendation.
- Active: (the default). Information people might appreciate knowing about when it arrives, like a score update on their favorite sports team.
- Time Sensitive: . Information that directly impacts the person and requires their immediate attention, like an account security issue or a package delivery.
- Critical: . Urgent information about health and safety that directly impacts the person and demands their immediate attention. Critical notifications are extremely rare a
- Build trust by accurately representing the urgency of each notification
- Use the Time Sensitive interruption level only for notifications that are relevant in the moment
- Never use the Time Sensitive interruption level to send a marketing notification
- Get people’s permission if you want to send them promotional or marketing notifications
- Make sure people can manage their notification settings within your app

## Modality
Modality is a design technique that presents content in a separate, dedicated mode that prevents interaction with the parent view and requires an explicit action to dismiss.
- Present content modally only when there’s a clear benefit
- Aim to keep modal tasks simple, short, and streamlined
- Take care to avoid creating a modal experience that feels like an app within your app
- Consider using a full-screen modal style for in-depth content or a complex task
- Always give people an obvious way to dismiss a modal view
- When necessary, help people avoid data loss by getting confirmation before closing a modal view
- Make it easy to identify a modal view’s task
- Let people dismiss a modal view before presenting another one

## Multitasking
Multitasking lets people switch quickly from one app to another, performing tasks in each.
- Pause activities that require people’s attention or active participation when they switch away
- Respond smoothly to audio interruptions
- Finish user-initiated tasks in the background
- Use notifications sparingly

## Offering help
Although the most effective experiences are approachable and intuitive, you can provide contextual help when necessary.
- Let your app’s tasks inform the types of help people might need
- Use relevant and consistent language and images in your help content
- Make sure all help content is inclusive
- Avoid bloating your help content by explaining how standard components or patterns work
- Use the most appropriate tip type for your app’s user interface
- Use tips for simple features
- Make tips short, actionable, and engaging
- Define rules to help ensure your tips reach the intended audience
- If there’s an image or symbol that people associate with the feature, consider including it in the tip, and prefer the filled variant
- Use buttons to direct people to information or options

## Onboarding
Onboarding can help people get a quick start using your app or game.
- Teach through interactivity
- Consider providing a collection of context-specific tips instead of a single onboarding flow
- If you need to present a prerequisite onboarding flow, design a brief, enjoyable experience that doesn’t require people to memorize a lot of information
- If it makes sense to offer a separate tutorial, consider making it optional
- Keep onboarding content focused on the experience you provide
- Briefly display a splash screen if necessary
- Don’t let large downloads hinder onboarding
- Avoid displaying licensing details within your onboarding flow
- Postpone nonessential setup flows or customization steps
- If your app or game needs access to private data or resources before it can function, consider integrating the permission request into your onboarding flow
- Prefer letting people experience your app or game before prompting them for ratings or purchases

## Playing audio
People expect rich audio experiences that automatically adjust when the context changes on the device.
- Adjust levels automatically when necessary — don’t adjust the overall volume
- Permit rerouting of audio when possible
- Use the system-provided volume view to let people make audio adjustments
- Choose an audio category that fits the way your app or game uses sound
- Respond to audio controls only when it makes sense
- Avoid repurposing audio controls
- Consider creating custom audio player controls only if you need to offer commands that the system doesn’t support
- Let other apps know when your app finishes playing temporary audio
- Determine how to respond to audio-session interruptions
- When an interruption ends, determine whether to resume audio playback automatically

## Playing haptics
Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game.
- Use system-provided haptic patterns according to their documented meanings
- Use haptics consistently throughout your app or game
- Prefer using haptics to complement other feedback in your app or game
- Avoid overusing haptics
- In most apps, prefer playing short haptics that complement discrete events
- Make haptics optional
- Be aware that playing haptics might impact other user experiences
- Transient: events are brief and compact, often feeling like taps or impulses. The experience of tapping the Flashlight button on the Home Screen is an example of a transie
- Continuous: events feel like sustained vibrations, such as the experience of the lasers effect in a message.

## Playing video
People expect to enjoy rich video experiences on their devices, regardless of the app or game they’re using.
- Use the system video player to give people a familiar and convenient experience
- Always display video content at its original aspect ratio
- [tab] Result of padding a 4:3 video
- [tab] Result of padding a 21:9 video
- Provide additional information when it adds value
- Support the interactions people expect, regardless of the input device they’re using to control playback
- If people need to access playback options or content-specific information in your tvOS app, consider adding a transport control or a custom content tab
- Avoid allowing audio from different sources to mix as viewers switch between modes
- Ensure a smooth transition to your app
- Show the expected content immediately
- Avoid asking people if they want to resume playback
- Play or pause playback when people press Space on a connected Bluetooth keyboard
- Make sure content plays for the correct viewer
- Use the previous end time when resuming playback of a long video clip
- Avoid displaying loading screens when possible
- Start playback immediately
- Minimize loading screen content
- Show a contextually relevant screen
- Be prepared for an immediate exit

## Printing
An iOS, iPadOS, macOS, or visionOS app can integrate system-provided print functionality when it makes sense, presenting custom printer- and document-specific options if necessary.
- Make printing discoverable
- Present a printing option only when it’s possible
- Present relevant printing options

## Ratings and reviews
People often view the ratings and reviews for an app or game before they download it.
- Ask for a rating only after people have demonstrated engagement with your app or game
- Avoid interrupting people while they’re performing a task or playing a game
- Avoid pestering people
- Prefer the system-provided prompt
- Weigh the benefits of resetting your summary rating against the potential disadvantage of showing fewer ratings

## Searching
People use various search techniques to find content on their device, within an app, and within a document or file.
- If search is important, give it a primary position in your app or view
- Aim to make your app’s content searchable through a single location
- Clearly display the current scope of a search
- Provide suggestions to make searching easier
- Take privacy into consideration before displaying search history
- Make your app’s content searchable in Spotlight
- Define metadata for custom file types you handle
- Use Spotlight to offer advanced file-search capabilities within the context of your app
- Prefer using the system-provided open and save views
- Implement a Quick Look generator if your app produces custom file types

## Settings
People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.
- Aim to provide default settings that give the best experience to the largest number of people
- Minimize the number of settings you offer
- Make settings available in ways people expect
- Avoid using settings to ask for setup information you can get in other ways
- Respect people’s systemwide settings and avoid including redundant versions of them in your custom settings area
- Put general, infrequently changed settings in your custom settings area
- When possible, prefer letting people modify task-specific options without going to your settings area
- Add only the most rarely changed options to the system-provided Settings app

## Undo and redo
Undo and redo gives people easy ways to reverse many types of actions, which can also help people explore and experiment safely as they learn a new interface or task.
- Help people predict the results of undo and redo as much as possible
- Show the results of an undo or redo
- Let people undo multiple times
- Consider giving people the option to revert multiple changes at once
- Provide undo and redo buttons only when necessary

## Workouts
A great workout or fitness experience encourages people to engage with their current activity and helps them track their progress on their devices.
- In a watchOS fitness app, use workout sessions to provide useful data and relevant controls
- Avoid distracting people from a workout with information that’s not relevant
- Use a distinct visual appearance to indicate an active workout
- Provide workout controls that are easy to find and tap
- Help people understand the health information your app records if sensor data is unavailable during a workout
- Provide a summary at the end of a session
- Discard extremely brief workout sessions
- Make sure text is legible for when people are in motion
- Use Activity rings correctly
