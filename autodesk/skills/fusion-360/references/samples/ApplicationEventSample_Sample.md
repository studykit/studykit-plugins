# Application Event API Sample

## Description

Add-In that demonstrates application events. To use this sample, create a new folder using the name you want to use for the new add-in. Inside the folder, create a new file that is the same name as the folder but has a .py extension. Copy the code below into the .py file. Create another file that is the same name as the folder but has a .manifest extension and copy the JSON data below into that file.
{
"autodeskProduct": "Fusion360",
"type": "addin",
"author": "",
"description": {
"": ""
},
"supportedOS": "windows|mac",
"editEnabled": true
}
Run the "Scripts and Add-Ins" command and click the green plus button near the top of the dialog. Browse to the location where you created the folder and select the folder. The add-in should now be displayed in the list of add-ins on the "Add-Ins" tab of the dialog. Select the add-in and click the "Run" button. This will load the add-in and when any of the application events occurr that it is watching for it will report them in the TEXT COMMAND window.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/ApplicationEvents.h>
#include <Core/Application/DocumentEvents.h>
#include <Core/UserInterface/UserInterface.h>

using namespace adsk::core;

Ptr<Application> app;
Ptr<UserInterface> ui;

// Event handler for the documentCreated event.
class MyDocumentCreatedEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        // Code to react to the event.
        ui->messageBox("In MyDocumentCreatedEventHandler event handler.");
    }
} documentCreated_;

// Event handler for the documentSaved event.
class MyDocumentSavedEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        // Code to react to the event.
        ui->messageBox("In MyDocumentSavedEventHandler event handler.");
    }
} documentSaved_;

// Event handler for the documentSaving event.
class MyDocumentSavingEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        // Code to react to the event.
        ui->messageBox("In MyDocumentSavingEventHandler event handler.");
    }
} documentSaving_;

// Event handler for the documentClosed event.
class MyDocumentClosedEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        // Code to react to the event.
        ui->messageBox("In MyDocumentClosedEventHandler event handler.");
    }
} documentClosed_;

// Event handler for the documentClosing event.
class MyDocumentClosingEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        // Code to react to the event.
        ui->messageBox("In MyDocumentClosingEventHandler event handler.");
    }
} documentClosing_;

class MyDocumentActivatedEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        Ptr<Document> doc = eventArgs->document();

        // Code to react to the event.
        ui->messageBox("In MyDocumentActivatedEventHandler event handler.");
    }
} documentActivated_;

class MyDocumentDeactivatedEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        Ptr<Document> doc = eventArgs->document();

        // Code to react to the event.
        ui->messageBox("In MyDocumentDeactivatedEventHandler event handler.");
    }
} documentDeactivated_;

class MyDocumentDeactivatingEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        Ptr<Document> doc = eventArgs->document();

        // Code to react to the event.
        ui->messageBox("In MyDocumentDeactivatingEventHandler event handler.");
    }
} documentDeactivating_;

class MyDocumentActivatingEventHandler : public adsk::core::DocumentEventHandler
{
  public:
    void notify(const Ptr<DocumentEventArgs>& eventArgs) override
    {
        Ptr<Document> doc = eventArgs->document();

        // Code to react to the event.
        ui->messageBox("In MyDocumentActivatingEventHandler event handler.");
    }
} documentActivating_;

class StartupCompletedHandler : public ApplicationEventHandler
{
  public:
    void notify(const Ptr<ApplicationEventArgs>& eventArgs) override
    {
        if (ui)
            ui->messageBox("Startup completed");
    }
};
static StartupCompletedHandler startupCompletedHandler_;

class OnlineStatusChangedHandler : public ApplicationEventHandler
{
  public:
    void notify(const Ptr<ApplicationEventArgs>& eventArgs) override
    {
        if (!eventArgs)
            return;

        std::string status("Online");
        if (eventArgs->isOffLine())
            status = "Offline";

        if (ui)
            ui->messageBox("Online status changed: " + status);
    }
};
static OnlineStatusChangedHandler onlineStatusChangedHandler_;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    Ptr<ApplicationEvent> startupCompleted = app->startupCompleted();
    if (!startupCompleted)
        return false;
    startupCompleted->add(&startupCompletedHandler_);

    Ptr<ApplicationEvent> onlineStatusChanged = app->onlineStatusChanged();
    if (!onlineStatusChanged)
        return false;
    onlineStatusChanged->add(&onlineStatusChangedHandler_);

    Ptr<DocumentEvent> documentCreated = app->documentCreated();
    if (!documentCreated)
        return false;
    documentCreated->add(&documentCreated_);

    Ptr<DocumentEvent> documentSaved = app->documentSaved();
    if (!documentSaved)
        return false;
    documentSaved->add(&documentSaved_);

    Ptr<DocumentEvent> documentSaving = app->documentSaving();
    if (!documentSaving)
        return false;
    documentSaving->add(&documentSaving_);

    Ptr<DocumentEvent> documentClosed = app->documentClosed();
    if (!documentClosed)
        return false;
    documentClosed->add(&documentClosed_);

    Ptr<DocumentEvent> documentClosing = app->documentClosing();
    if (!documentClosing)
        return false;
    documentClosing->add(&documentClosing_);

    Ptr<DocumentEvent> documentActivated = app->documentActivated();
    if (!documentActivated)
        return false;
    documentActivated->add(&documentActivated_);

    Ptr<DocumentEvent> documentActivating = app->documentActivating();
    if (!documentActivating)
        return false;
    documentActivating->add(&documentActivating_);

    Ptr<DocumentEvent> documentDeactivating = app->documentDeactivating();
    if (!documentDeactivating)
        return false;
    documentDeactivating->add(&documentDeactivating_);

    Ptr<DocumentEvent> documentDeactivated = app->documentDeactivated();
    if (!documentDeactivated)
        return false;
    documentDeactivated->add(&documentDeactivated_);

    return true;
}

extern "C" XI_EXPORT bool stop(const char* context)
{
    return true;
}
```

|  |
| --- |
| Copy Code |

```
import adsk.core, traceback

# global set of event handlers to keep them referenced
handlers = []
app = adsk.core.Application.get()

# Event handler for the documentOpened event.
class MyDocumentOpenedHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentOpenedHandler event handler.')

# Event handler for the documentOpening event.
class MyDocumentOpeningHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentOpeningHandler event handler.')

# Event handler for the startupCompleted event.
class StartupCompletedHandler(adsk.core.ApplicationEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
           app.log('Startup completed')
        except:
           app.log('Startup completed event failed: {}'.format(traceback.format_exc()))

# Event handler for the onlineStatusChanged event.
class OnlineStatusChangedHandler(adsk.core.ApplicationEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
           status = 'Online'
           if args.isOffLine:
               status = 'Offline'
           app.log('Online status changed: ' + status)
        except:
           app.log('Online status changed event failed: {}'.format(traceback.format_exc()))

# Event handler for the documentCreated event.
class MyDocumentCreatedHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentCreatedHandler event handler.')

# Event handler for the documentSaved event.
class MyDocumentSavedHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentSavedHandler event handler.')

# Event handler for the documentSaving event.
class MyDocumentSavingHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentSavingHandler event handler.')

# Event handler for the documentClosing event.
class MyDocumentClosingHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentClosingHandler event handler.')

# Event handler for the documentClosed event.
class MyDocumentClosedHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentClosedHandler event handler.')

# Event handler for the documentDeactivated event.
class MyDocumentDeactivatedHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentDeactivatedHandler event handler.\ndocument: {}'.format(eventArgs.document.name))

# Event handler for the documentActivated event.
class MyDocumentActivatedHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentActivatedHandler event handler.\ndocument: {}'.format(eventArgs.document.name))

# Event handler for the documentDeactivating event.
class MyDocumentDeactivatingHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentDeactivatingHandler event handler.\ndocument: {}'.format(eventArgs.document.name))

# Event handler for the documentActivating event.
class MyDocumentActivatingHandler(adsk.core.DocumentEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.DocumentEventArgs.cast(args)

        # Code to react to the event.
        app.log('In MyDocumentActivatingHandler event handler.\ndocument: {}'.format(eventArgs.document.name))

def run(context):
    try:
        onStartupCompleted = StartupCompletedHandler()
        app.startupCompleted.add(onStartupCompleted)
        handlers.append(onStartupCompleted)

        onOnlineStatusChanged = OnlineStatusChangedHandler()
        app.onlineStatusChanged.add(onOnlineStatusChanged)
        handlers.append(onOnlineStatusChanged)

        onDocumentCreated = MyDocumentCreatedHandler()
        app.documentCreated.add(onDocumentCreated)
        handlers.append(onDocumentCreated)

        onDocumentSaved = MyDocumentSavedHandler()
        app.documentSaved.add(onDocumentSaved)
        handlers.append(onDocumentSaved)

        onDocumentSaving = MyDocumentSavingHandler()
        app.documentSaving.add(onDocumentSaving)
        handlers.append(onDocumentSaving)

        onDocumentOpened = MyDocumentOpenedHandler()
        app.documentOpened.add(onDocumentOpened)
        handlers.append(onDocumentOpened)

        onDocumentOpening = MyDocumentOpeningHandler()
        app.documentOpening.add(onDocumentOpening)
        handlers.append(onDocumentOpening)

        onDocumentClosing = MyDocumentClosingHandler()
        app.documentClosing.add(onDocumentClosing)
        handlers.append(onDocumentClosing)

        onDocumentClosed = MyDocumentClosedHandler()
        app.documentClosed.add(onDocumentClosed)
        handlers.append(onDocumentClosed)

        onDocumentDeactivated = MyDocumentDeactivatedHandler()
        app.documentDeactivated.add(onDocumentDeactivated)
        handlers.append(onDocumentDeactivated)

        onDocumentActivated = MyDocumentActivatedHandler()
        app.documentActivated.add(onDocumentActivated)
        handlers.append(onDocumentActivated)

        onDocumentDeactivating = MyDocumentDeactivatingHandler()
        app.documentDeactivating.add(onDocumentDeactivating)
        handlers.append(onDocumentDeactivating)

        onDocumentActivating = MyDocumentActivatingHandler()
        app.documentActivating.add(onDocumentActivating)
        handlers.append(onDocumentActivating)
    except:
        app.log('AddIn Start Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        pass
    except:
        app.log('AddIn Stop Failed: {}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |