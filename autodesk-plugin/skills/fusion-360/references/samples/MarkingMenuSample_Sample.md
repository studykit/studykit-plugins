# Marking Menu API Sample

## Description

Demonstrates how to customize marking menu and context menu. This sample is an add-in. To use it, create a new add-in using the "Scrips and Add-Ins" command. Use any name you would like for the add-in. In the folder where the add-in was created edit the *add-in name*.py file and replace it's entire contents with the sample code below. You can also delete all the other files that were created for the add-in except for *add-in name*.manifiest. Start the add-in from the "Scripts and Add-Ins" dialog. Now, with the add-in running, whenever you right-click in the Fusion window, you'll get an entirely customized context menu. The default marking menu has been modified by the add-in by removing the existing commands and adding some custom commands.

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
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/UserInterface/CommandCreatedEventHandler.h>
#include <Core/UserInterface/CommandCreatedEvent.h>
#include <Core/UserInterface/CommandCreatedEventArgs.h>
#include <Core/UserInterface/CommandEvent.h>
#include <Core/UserInterface/CommandEventArgs.h>
#include <Core/UserInterface/CommandEventHandler.h>
#include <Core/UserInterface/MarkingMenuEvent.h>
#include <Core/UserInterface/MarkingMenuEventArgs.h>
#include <Core/UserInterface/MarkingMenuEventHandler.h>
#include <Core/UserInterface/RadialMarkingMenu.h>
#include <Core/UserInterface/LinearMarkingMenu.h>
#include <Core/UserInterface/Command.h>
#include <Core/UserInterface/CommandDefinition.h>
#include <Core/UserInterface/CommandDefinitions.h>
#include <Core/UserInterface/ToolbarControls.h>
#include <Core/UserInterface/DropDownControl.h>
#include <Core/UserInterface/Selection.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepEdge.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepVertex.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/SketchEntity.h>
#include <Fusion/Construction/ConstructionPlane.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;
Ptr<UserInterface> ui;
std::vector<Ptr<Base>> entities;
static void setLinearMarkingMenu(const Ptr<MarkingMenuEventArgs>& eventArgs)
{
    Ptr<CommandDefinitions> definitions = ui->commandDefinitions();
    if (!definitions)
        return;
    Ptr<CommandDefinition> cmdDefSelectedEntities = definitions->itemById("PrintSelectedEntities");
    Ptr<CommandDefinition> cmdDef = definitions->itemById("TestCommand");
    if (!cmdDef || !cmdDefSelectedEntities)
        return;

    Ptr<LinearMarkingMenu> linearMenu = eventArgs->linearMarkingMenu();
    if (!linearMenu)
        return;
    // Clear current linear menu
    linearMenu->clear();

    // Add test command, add print-entity command
    Ptr<ToolbarControls> controls = linearMenu->controls();
    controls->addCommand(cmdDef);
    controls->addCommand(cmdDefSelectedEntities);
    // Add a separator line
    controls->addSeparator("LinearSeparator");
    // Add a sub linear menu
    Ptr<DropDownControl> dropdown = controls->addDropDown("Linear Sub Menu", "", "LinearSubMenu");
    Ptr<ToolbarControls> subControls = dropdown->controls();
    subControls->addCommand(cmdDef);
    subControls->addCommand(cmdDefSelectedEntities);
    // Add a sub-sub linear menu
    if (!subControls)
        return;
    Ptr<DropDownControl> subDropdown = subControls->addDropDown("Linear sub-sub menu", "", "LinearSubSub");
    Ptr<ToolbarControls> subsubControls = subDropdown->controls();
    subsubControls->addCommand(cmdDef);
    subsubControls->addCommand(cmdDefSelectedEntities);

    // Add some special command if selecting BRep/sketch entities.
    std::vector<Ptr<Base>> selectedEntities = eventArgs->selectedEntities();
    if (selectedEntities.size())
    {
        Ptr<Base> sel0 = selectedEntities[0];
        // special command if BRep entity selected
        if (sel0->query<BRepFace>() || sel0->query<BRepEdge>() || sel0->query<BRepBody>() || sel0->query<BRepVertex>())
        {
            Ptr<CommandDefinition> cmdDefBRepSpecial = definitions->itemById("BrepCommand");
            controls->addCommand(cmdDefBRepSpecial);
        }
        // special command if sketch entity selected
        if (sel0->query<Sketch>() || sel0->query<Profile>() || sel0->query<SketchEntity>())
        {
            Ptr<CommandDefinition> cmdDefSketchSpecial = definitions->itemById("SketchCommand");
            controls->addCommand(cmdDefSketchSpecial);
        }
    }
}

static void setRadialMarkingMenu(const Ptr<MarkingMenuEventArgs>& eventArgs)
{
    Ptr<CommandDefinitions> definitions = ui->commandDefinitions();
    if (!definitions)
        return;
    Ptr<CommandDefinition> cmdDefSelectedEntities = definitions->itemById("PrintSelectedEntities");
    Ptr<CommandDefinition> cmdDef = definitions->itemById("TestCommand");
    if (!cmdDef || !cmdDefSelectedEntities)
        return;

    Ptr<RadialMarkingMenu> radialMenu = eventArgs->radialMarkingMenu();
    if (!radialMenu)
        return;

    // Clear current radial menu
    radialMenu->clear();

    // Create sub radial menu
    Ptr<RadialMarkingMenu> subRadial = radialMenu->create("test");
    subRadial->text("sub");

    // Create sub-sub radial menu
    Ptr<RadialMarkingMenu> subsubRadial = subRadial->create("sub sub");

    // sub-sub radial menu layout
    subsubRadial->westCommand(cmdDef);
    subsubRadial->northCommand(cmdDef);
    subsubRadial->southCommand(cmdDefSelectedEntities);
    subsubRadial->eastCommand(cmdDef);

    // sub radial menu layout
    subRadial->northwestCommand(subsubRadial);
    subRadial->southeastCommand(cmdDef);
    subRadial->southwestCommand(cmdDef);
    subRadial->northeastCommand(cmdDefSelectedEntities);

    // root radial menu layout
    radialMenu->westCommand(cmdDef);
    radialMenu->northCommand(cmdDef);
    radialMenu->southCommand(cmdDef);
    radialMenu->eastCommand(cmdDef);
    radialMenu->northeastCommand(subRadial);
    radialMenu->northwestCommand(cmdDefSelectedEntities);
    radialMenu->southeastCommand(cmdDef);
    radialMenu->southwestCommand(cmdDef);
}

class MyMarkingMenuHandler : public adsk::core::MarkingMenuEventHandler
{
  public:
    void notify(const Ptr<MarkingMenuEventArgs>& eventArgs) override
    {
        setLinearMarkingMenu(eventArgs);
        setRadialMarkingMenu(eventArgs);

        entities.clear();
        entities = eventArgs->selectedEntities();
    }
} onMarkingMenuDisplaying_;

class CommandExecutedHandler : public adsk::core::CommandEventHandler
{
  public:
    void notify(const Ptr<CommandEventArgs>& eventArgs) override
    {
        Ptr<Event> firingEvent = eventArgs->firingEvent();
        if (!firingEvent)
            return;

        Ptr<Command> command = firingEvent->sender();
        if (!command)
            return;

        Ptr<CommandDefinition> parentDefinition = command->parentCommandDefinition();
        if (!parentDefinition)
            return;

        Ptr<MarkingMenuEvent> markingMenuEvent = ui->markingMenuDisplaying();
        if (!markingMenuEvent)
            return;

        if (parentDefinition->id() == "PrintSelectedEntities")
        {
            if (!entities.empty())
            {
                std::string msg = "selected entities:";
                for (Ptr<Base> obj : entities)
                {
                    msg += '\n' + obj->objectType();
                }
                ui->messageBox(msg);
            }
            else
            {
                ui->messageBox("No selected entity.");
            }
        }
        else
        {
            ui->messageBox("command " + parentDefinition->id() + " triggered");
        }
    }
};

class CommandCreatedHandler : public adsk::core::CommandCreatedEventHandler
{
  public:
    void notify(const Ptr<CommandCreatedEventArgs>& eventArgs) override
    {
        if (eventArgs)
        {
            Ptr<Command> command = eventArgs->command();
            if (!command)
                return;

            Ptr<CommandEvent> exec = command->execute();
            if (!exec)
                return;
            exec->add(&onCommandExecuted_);
        }
    }

  private:
    CommandExecutedHandler onCommandExecuted_;
} onCommandCreated_;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    // Add customized handler for marking menu displaying
    Ptr<MarkingMenuEvent> markingMenuEvent = ui->markingMenuDisplaying();
    if (!markingMenuEvent)
        return false;
    markingMenuEvent->add(&onMarkingMenuDisplaying_);

    // Add customized handler for marking menu displaying
    // Create a command to print selected entities
    Ptr<CommandDefinitions> definitions = ui->commandDefinitions();
    if (!definitions)
        return false;
    Ptr<CommandDefinition> cmdDefSelectedEntities = definitions->itemById("PrintSelectedEntities");
    if (!cmdDefSelectedEntities)
    {
        cmdDefSelectedEntities =
            definitions->addButtonDefinition("PrintSelectedEntities", "Print Entities", "Print selected entities.");
        if (!cmdDefSelectedEntities)
            return false;
        Ptr<CommandCreatedEvent> printCmdCreatedEvent = cmdDefSelectedEntities->commandCreated();
        if (!printCmdCreatedEvent)
            return false;
        printCmdCreatedEvent->add(&onCommandCreated_);
    }

    // Create a test command
    Ptr<CommandDefinition> cmdDef = definitions->itemById("TestCommand");
    if (!cmdDef)
    {
        cmdDef = definitions->addButtonDefinition("TestCommand", "Test Command", "Test Command");
        if (!cmdDef)
            return false;
        Ptr<CommandCreatedEvent> testCmdCreatedEvent = cmdDef->commandCreated();
        if (!testCmdCreatedEvent)
            return false;
        testCmdCreatedEvent->add(&onCommandCreated_);
    }

    // Create special command for BRep entities
    Ptr<CommandDefinition> cmdDefBRepSpecial = definitions->itemById("BrepCommand");
    if (!cmdDefBRepSpecial)
    {
        cmdDefBRepSpecial =
            definitions->addButtonDefinition("BrepCommand", "Brep Command", "This is a command for BRep entities.");
        if (!cmdDefBRepSpecial)
            return false;
        Ptr<CommandCreatedEvent> brepCmdCreatedEvent = cmdDefBRepSpecial->commandCreated();
        if (!brepCmdCreatedEvent)
            return false;
        brepCmdCreatedEvent->add(&onCommandCreated_);
    }

    // Create special command for sketch entities
    Ptr<CommandDefinition> cmdDefSketchSpecial = definitions->itemById("SketchCommand");
    if (!cmdDefSketchSpecial)
    {
        cmdDefSketchSpecial = definitions->addButtonDefinition(
            "SketchCommand", "Sketch Command", "This is a command for sketch entities.");
        if (!cmdDefSketchSpecial)
            return false;
        Ptr<CommandCreatedEvent> sketchCmdCreatedEvent = cmdDefSketchSpecial->commandCreated();
        if (!sketchCmdCreatedEvent)
            return false;
        sketchCmdCreatedEvent->add(&onCommandCreated_);
    }

    // prevent this module from being terminate when the script returns, because we are waiting for event handlers to
    // fire
    adsk::autoTerminate(false);

    ui->messageBox("Right click to see the customized marking menu.");

    return true;
}

extern "C" XI_EXPORT bool stop(const char* context)
{
    if (ui)
    {
        Ptr<CommandDefinitions> definitions = ui->commandDefinitions();
        if (!definitions)
            return false;

        Ptr<CommandDefinition> cmdDefSelectedEntities = definitions->itemById("PrintSelectedEntities");
        if (cmdDefSelectedEntities)
            cmdDefSelectedEntities->deleteMe();

        Ptr<CommandDefinition> cmdDef = definitions->itemById("TestCommand");
        if (cmdDef)
            cmdDef->deleteMe();

        Ptr<CommandDefinition> cmdDefBRepSpecial = definitions->itemById("BrepCommand");
        if (cmdDefBRepSpecial)
            cmdDefBRepSpecial->deleteMe();

        Ptr<CommandDefinition> cmdDefSketchSpecial = definitions->itemById("SketchCommand");
        if (cmdDefSketchSpecial)
            cmdDefSketchSpecial->deleteMe();

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

# global mapping list of event handlers to keep them referenced for the duration of the command
#handlers = {}
handlers = []
cmdDefs = []
entities = []

def run(context):
    ui = None
    handlers.clear()
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        def setLinearMarkingMenu(args):
            try:
                menuArgs = adsk.core.MarkingMenuEventArgs.cast(args)
                cmdDefSelectedEntities = ui.commandDefinitions.itemById('PrintSelectedEntities')
                cmdDef = ui.commandDefinitions.itemById('TestCommand')

                commands = []
                commands.append(cmdDefSelectedEntities)
                commands.append(cmdDef)

                linearMenu = menuArgs.linearMarkingMenu
                # linear
                linearMenu.clear()
                linearMenu.controls.addCommand(cmdDef)
                linearMenu.controls.addCommand(cmdDefSelectedEntities)
                linearMenu.controls.addSeparator('LinearSeparator')
                dropdown = linearMenu.controls.addDropDown('Linear Sub Menu', '', 'LinearSubMenu')
                subDropDown = dropdown.controls.addDropDown('sub sub', '', 'Sub Sub')
                for cmd in commands:
                    dropdown.controls.addCommand(cmd)
                    subDropDown.controls.addCommand(cmd)

                if args.selectedEntities:
                    sel0 = args.selectedEntities[0]
                    # special command if brep entities selected
                    body = adsk.fusion.BRepBody.cast(sel0)
                    face = adsk.fusion.BRepFace.cast(sel0)
                    edge = adsk.fusion.BRepEdge.cast(sel0)
                    vertex = adsk.fusion.BRepVertex.cast(sel0)
                    if body or face or edge or vertex:
                        cmdDefSpecial = ui.commandDefinitions.itemById('BrepCommand')
                        linearMenu.controls.addCommand(cmdDefSpecial)

                    # special command if sketch entities selected
                    sketch = adsk.fusion.Sketch.cast(sel0)
                    prof = adsk.fusion.Profile.cast(sel0)
                    sketchEntity = adsk.fusion.SketchEntity.cast(sel0)
                    if sketch or sketchEntity or prof:
                        cmdDefSpecial = ui.commandDefinitions.itemById('SketchCommand')
                        linearMenu.controls.addCommand(cmdDefSpecial)
            except:
                if ui:
                    ui.messageBox('setting linear menu failed: {}').format(traceback.format_exc())

        def setRadialMarkingMenu(args):
            try:
                menuArgs = adsk.core.MarkingMenuEventArgs.cast(args)
                cmdDefSelectedEntities = ui.commandDefinitions.itemById('PrintSelectedEntities')
                cmdDef = ui.commandDefinitions.itemById('TestCommand')

                radialMenu = menuArgs.radialMarkingMenu
                # radial
                radialMenu.clear()

                subRadial = radialMenu.create("test")
                subRadial.text = "sub"

                subsubRadial = subRadial.create('sub sub')
                # sub sub
                subsubRadial.westCommand = cmdDef
                subsubRadial.northCommand = cmdDef
                subsubRadial.southCommand = cmdDefSelectedEntities
                subsubRadial.eastCommand = cmdDef

                # sub radial menu
                subRadial.northwestCommand = subsubRadial
                subRadial.southeastCommand = cmdDef
                subRadial.southwestCommand = cmdDef
                subRadial.northeastCommand = cmdDefSelectedEntities

                # root radial menu
                radialMenu.eastCommand = cmdDef
                radialMenu.westCommand = cmdDef
                radialMenu.northCommand = cmdDef
                radialMenu.southCommand = cmdDef
                radialMenu.northeastCommand = subRadial
                radialMenu.northwestCommand = cmdDefSelectedEntities
                radialMenu.southeastCommand = cmdDef
                radialMenu.southwestCommand = cmdDef

            except:
                if ui:
                    ui.messageBox('setting radial menu failed: {}').format(traceback.format_exc())

        class MyCommandCreatedEventHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    command = args.command
                    onCommandExcute = MyCommandExecuteHandler()
                    handlers.append(onCommandExcute)
                    command.execute.add(onCommandExcute)
                except:
                    ui.messageBox('command created failed: {}').format(traceback.format_exc())

        class MyCommandExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    command = args.firingEvent.sender
                    cmdDef = command.parentCommandDefinition
                    if cmdDef:
                        if cmdDef.id == 'PrintSelectedEntities':
                            if entities:
                                entityList = 'selected entities:'
                                for e in entities:
                                    entityList += '\n' + str(e)
                                ui.messageBox(entityList)
                            else:
                                ui.messageBox('No selected entity.')
                        else:
                            ui.messageBox('command {} triggered.'.format(cmdDef.id))
                    else:
                        ui.messageBox('No CommandDefinition')
                except:
                    if ui:
                        ui.messageBox('command executed failed: {}').format(traceback.format_exc())

        class MyMarkingMenuHandler(adsk.core.MarkingMenuEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    setLinearMarkingMenu(args)
                    setRadialMarkingMenu(args)

                    # selected entities
                    global entities
                    entities.clear()
                    entities = args.selectedEntities
                except:
                    if ui:
                        ui.messageBox('Marking Menu Displaying event failed: {}'.format(traceback.format_exc()))

        # Add customized handler for marking menu displaying
        onMarkingMenuDisplaying = MyMarkingMenuHandler()
        handlers.append(onMarkingMenuDisplaying)
        ui.markingMenuDisplaying.add(onMarkingMenuDisplaying)

        # Add customized handler for commands creating
        onCommandCreated = MyCommandCreatedEventHandler()
        handlers.append(onCommandCreated)

        # Create a command to print selected entities
        cmdDefSelectedEntities = ui.commandDefinitions.itemById('PrintSelectedEntities')
        if not cmdDefSelectedEntities:
            cmdDefSelectedEntities = ui.commandDefinitions.addButtonDefinition('PrintSelectedEntities', 'Print Entities', 'Print selected entities.')
            cmdDefSelectedEntities.commandCreated.add(onCommandCreated)
            cmdDefs.append(cmdDefSelectedEntities)

        # Create a test command
        cmdDef = ui.commandDefinitions.itemById('TestCommand')
        if not cmdDef:
            cmdDef = ui.commandDefinitions.addButtonDefinition('TestCommand', 'Test Command', 'Test Command')
            cmdDef.commandCreated.add(onCommandCreated)
            cmdDefs.append(cmdDef)

        # Create special command for brep entities
        cmdDefBRepSpecial = ui.commandDefinitions.itemById('BrepCommand')
        if not cmdDefBRepSpecial:
            cmdDefBRepSpecial = ui.commandDefinitions.addButtonDefinition('BrepCommand', 'Brep Command', 'This is a command for brep entities.')
            cmdDefBRepSpecial.commandCreated.add(onCommandCreated)
            cmdDefs.append(cmdDefBRepSpecial)

        # Create special command for sketch entities
        cmdDefSketchSpecial = ui.commandDefinitions.itemById('SketchCommand')
        if not cmdDefSketchSpecial:
            cmdDefSketchSpecial = ui.commandDefinitions.addButtonDefinition('SketchCommand', 'Sketch Command', 'This is a command for sketch entities.')
            cmdDefSketchSpecial.commandCreated.add(onCommandCreated)
            cmdDefs.append(cmdDefSketchSpecial)

        ui.messageBox('Right click to see the customized marking menu.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        for obj in cmdDefs:
            if obj.isValid:
                obj.deleteMe()
            else:
                ui.messageBox(str(obj) + ' is not a valid object')

        handlers.clear()

        ui.messageBox('Stop addin')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |