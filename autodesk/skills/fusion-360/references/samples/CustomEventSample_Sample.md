# Custom Event Sample

## Description

Demonstrates the ability to call into the main thread from a worker thread. This sample is an **add-in**. To use it, use the **Scripts and Add-Ins** command to create a new add-in. Delete all of the code in the newly created add-in and replace it with the code below. Have a model open that has a parameter named "Length". Load the add-in. The add-in will change the value of the parameter every two seconds using a random value between 1 and 10.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/Utils.h>
#include <Core/Application/Application.h>
#include <Core/Application/Product.h>
#include <Core/Application/CustomEvents.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/UserInterface/CommandDefinitions.h>
#include <Core/UserInterface/CommandDefinition.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Fusion/ModelParameters.h>
#include <Fusion/Fusion/ModelParameter.h>

#include <thread>
#include <sstream>
#include <chrono>
#include <random>

using namespace adsk::core;
using namespace adsk::fusion;

const std::string myCustomEvent = "MyCustomEventId1";

Ptr<Application> app;
Ptr<UserInterface> ui;
Ptr<CustomEvent> customEvent;
bool stopFlag;
std::default_random_engine generator;
std::uniform_int_distribution<int> distribution(1000, 10000);

class ThreadEventHandler : public CustomEventHandler
{
  public:
    void notify(const Ptr<CustomEventArgs>& eventArgs) override
    {
        if (eventArgs)
        {
            // Make sure a command isn't running before changes are made.
            if (ui->activeCommand() != "SelectCommand")
            {
                Ptr<CommandDefinitions> cmdDefs = ui->commandDefinitions();
                cmdDefs->itemById("SelectCommand")->execute();
            }

            Ptr<Design> design = app->activeProduct();
            if (!design)
                return;

            Ptr<Component> rootComp = design->rootComponent();
            if (!rootComp)
                return;

            Ptr<ModelParameters> params = rootComp->modelParameters();
            if (!params)
                return;

            Ptr<ModelParameter> param = params->itemByName("Length");
            if (!param)
                return;

            // Get the value that was passed in from other thread and set the paraemter value.
            std::string info = eventArgs->additionalInfo();
            param->value(std::stod(info));
        }
    }
} onCustomEvent_;

void myThreadRun()
{
    while (!stopFlag)
    {
        double randVal = distribution(generator);
        std::string additionalInfo = std::to_string(randVal / 1000.0);
        app->fireCustomEvent(myCustomEvent, additionalInfo);

        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
}

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    customEvent = app->registerCustomEvent(myCustomEvent);
    if (!customEvent)
        return false;
    customEvent->add(&onCustomEvent_);

    stopFlag = false;
    std::thread myThread(myThreadRun);
    myThread.detach();

    return true;
}

extern "C" XI_EXPORT bool stop(const char* context)
{
    if (ui)
    {
        customEvent->remove(&onCustomEvent_);
        stopFlag = true;
        app->unregisterCustomEvent(myCustomEvent);
        ui->messageBox("Stop addin");
        ui = nullptr;
    }

    return true;
}
```

|  |
| --- |
| Copy Code |

```
#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import threading, random, json

app = None
ui = adsk.core.UserInterface.cast(None)
handlers = []
stopFlag = None
myCustomEvent = 'MyCustomEventId'
customEvent = None

# The event handler that responds to the custom event being fired.
class ThreadEventHandler(adsk.core.CustomEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # Make sure a command isn't running before changes are made.
            if ui.activeCommand != 'SelectCommand':
                ui.commandDefinitions.itemById('SelectCommand').execute()

            # Get the value from the JSON data passed through the event.
            eventArgs = json.loads(args.additionalInfo)
            newValue = float(eventArgs['Value'])

            # Set the parameter value.
            design = adsk.fusion.Design.cast(app.activeProduct)
            param = design.rootComponent.modelParameters.itemByName('Length')
            param.value = newValue
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
            adsk.autoTerminate(False)

# The class for the new thread.
class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        # Every five seconds fire a custom event, passing a random number.
        while not self.stopped.wait(2):
            args = {'Value': random.randint(1000, 10000)/1000}
            app.fireCustomEvent(myCustomEvent, json.dumps(args))

def run(context):
    global ui
    global app
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Register the custom event and connect the handler.
        global customEvent
        customEvent = app.registerCustomEvent(myCustomEvent)
        onThreadEvent = ThreadEventHandler()
        customEvent.add(onThreadEvent)
        handlers.append(onThreadEvent)

        # Create a new thread for the other processing.
        global stopFlag
        stopFlag = threading.Event()
        myThread = MyThread(stopFlag)
        myThread.start()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        if handlers.count:
            customEvent.remove(handlers[0])
        stopFlag.set()
        app.unregisterCustomEvent(myCustomEvent)
        ui.messageBox('Stop addin')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |