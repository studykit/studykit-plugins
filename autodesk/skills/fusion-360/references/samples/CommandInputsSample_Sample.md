# Command Inputs API Sample

## Description

Creates a command dialog that demonstrates all of the available command inputs.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is.

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
#include <Core/Application/ValueInput.h>
#include <Core/Application/UnitsManager.h>
#include <Core/Application/ObjectCollection.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/UserInterface/CommandCreatedEventHandler.h>
#include <Core/UserInterface/CommandCreatedEvent.h>
#include <Core/UserInterface/CommandCreatedEventArgs.h>
#include <Core/UserInterface/CommandEvent.h>
#include <Core/UserInterface/CommandEventArgs.h>
#include <Core/UserInterface/CommandEventHandler.h>
#include <Core/UserInterface/InputChangedEvent.h>
#include <Core/UserInterface/InputChangedEventArgs.h>
#include <Core/UserInterface/InputChangedEventHandler.h>
#include <Core/UserInterface/Command.h>
#include <Core/UserInterface/CommandDefinition.h>
#include <Core/UserInterface/CommandDefinitions.h>
#include <Core/UserInterface/CommandInputs.h>
#include <Core/UserInterface/ValueCommandInput.h>
#include <Core/UserInterface/StringValueCommandInput.h>
#include <Core/UserInterface/TabCommandInput.h>
#include <Core/UserInterface/GroupCommandInput.h>
#include <Core/UserInterface/BoolValueCommandInput.h>
#include <Core/UserInterface/ButtonRowCommandInput.h>
#include <Core/UserInterface/DropDownCommandInput.h>
#include <Core/UserInterface/SelectionCommandInput.h>
#include <Core/UserInterface/FloatSliderCommandInput.h>
#include <Core/UserInterface/IntegerSliderCommandInput.h>
#include <Core/UserInterface/FloatSpinnerCommandInput.h>
#include <Core/UserInterface/IntegerSpinnerCommandInput.h>
#include <Core/UserInterface/RadioButtonGroupCommandInput.h>
#include <Core/UserInterface/ImageCommandInput.h>
#include <Core/UserInterface/ListItems.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/DirectionCommandInput.h>
#include <Core/UserInterface/DistanceValueCommandInput.h>
#include <Core/UserInterface/TableCommandInput.h>
#include <Core/UserInterface/AngleValueCommandInput.h>

#include <sstream>

using namespace adsk::core;

Ptr<Application> app;
Ptr<UserInterface> ui;

// Adds a new row to the table.
static void addRowToTable(Ptr<TableCommandInput> tableInput)
{
    if (!tableInput)
        return;

    // Define a unique id for each row.
    static int rowNumber = 0;
    std::stringstream rowId;
    rowId << rowNumber;

    // Get the CommandInputs object associated with the parent command.
    Ptr<CommandInputs> cmdInputs = tableInput->commandInputs();

    // Create three new command inputs.
    Ptr<CommandInput> childTableValueInput =
        cmdInputs->addValueInput("TableInput_value" + rowId.str(), "Value", "cm", ValueInput::createByReal(rowNumber));
    Ptr<CommandInput> childTableStringInput =
        cmdInputs->addStringValueInput("TableInput_string" + rowId.str(), "String", rowId.str());
    Ptr<CommandInput> childTableSpinnerInput =
        cmdInputs->addIntegerSpinnerCommandInput("spinnerInt" + rowId.str(), "Integer Spinner", 0, 100, 2, rowNumber);

    // Add the inputs to the table.
    int row = tableInput->rowCount();
    tableInput->addCommandInput(childTableValueInput, row, 0);
    tableInput->addCommandInput(childTableStringInput, row, 1);
    tableInput->addCommandInput(childTableSpinnerInput, row, 2);

    rowNumber = rowNumber + 1;
}

// Populate 'slider_configuration' group with as many sliders as set in 'slider_controller'.
// Delete previous ones and create new sliders.
static void updateSliders(Ptr<CommandInputs> sliderInputs)
{
    Ptr<IntegerSpinnerCommandInput> spinner = sliderInputs->itemById("slider_controller");
    if (!spinner)
    {
        return;
    }
    int value = spinner->value();
    // Check ranges
    if (value > spinner->maximumValue() || value < spinner->minimumValue())
    {
        return;
    }

    // Delete all sliders we have
    std::vector<Ptr<CommandInput>> toRemove;
    for (size_t i = 0; i < sliderInputs->count(); ++i)
    {
        Ptr<CommandInput> input = sliderInputs->item(i);
        if (input->objectType() == FloatSliderCommandInput::classType())
        {
            toRemove.push_back(input);
        }
    }
    for (auto input : toRemove)
    {
        input->deleteMe();
    }

    // Create new ones with range depending on total number
    for (int i = 1; i <= value; ++i)
    {
        std::string id = std::to_string(i);
        sliderInputs->addFloatSliderCommandInput("slider_configuration_" + id, "slider_" + id, "cm", 0, 10.0 * value);
    }
}

// InputChange event handler.
class OnInputChangedEventHander : public adsk::core::InputChangedEventHandler
{
  public:
    void notify(const Ptr<InputChangedEventArgs>& eventArgs) override
    {
        Ptr<CommandInputs> inputs = eventArgs->inputs();
        if (!inputs)
            return;

        Ptr<CommandInput> cmdInput = eventArgs->input();
        if (!cmdInput)
            return;

        // onInputChange for slider controller
        if (cmdInput->id() == "slider_controller")
        {
            Ptr<GroupCommandInput> sliderGroup = cmdInput->parentCommandInput();
            if (!sliderGroup)
            {
                return;
            }
            Ptr<CommandInputs> sliderInputs = sliderGroup->children();
            if (!sliderInputs)
            {
                return;
            }
            updateSliders(sliderInputs);
        }
        else
        {
            // Table handling
            Ptr<TableCommandInput> tableInput = inputs->itemById("table");
            if (!tableInput)
                return;

            if (cmdInput->id() == "tableAdd")
            {
                addRowToTable(tableInput);
            }
            else if (cmdInput->id() == "tableDelete")
            {
                if (tableInput->selectedRow() == -1)
                {
                    ui->messageBox("Select one row to delete.");
                }
                else
                {
                    tableInput->deleteRow(tableInput->selectedRow());
                }
            }
        }
    }
};

// CommandExecuted event handler.
class OnExecuteEventHander : public adsk::core::CommandEventHandler
{
  public:
    void notify(const Ptr<CommandEventArgs>& eventArgs) override
    {
    }
};

// CommandDestroyed event handler
class OnDestroyEventHandler : public adsk::core::CommandEventHandler
{
  public:
    void notify(const Ptr<CommandEventArgs>& eventArgs) override
    {
        adsk::terminate();
    }
};

// CommandCreated event handler.
class CommandCreatedEventHandler : public adsk::core::CommandCreatedEventHandler
{
  public:
    void notify(const Ptr<CommandCreatedEventArgs>& eventArgs) override
    {
        if (eventArgs)
        {
            // Get the command that was created.
            Ptr<Command> command = eventArgs->command();
            if (command)
            {
                // Connect to the command destroyed event.
                Ptr<CommandEvent> onDestroy = command->destroy();
                if (!onDestroy)
                    return;
                bool isOk = onDestroy->add(&onDestroyHandler);
                if (!isOk)
                    return;

                // Connect to the input changed event.
                Ptr<InputChangedEvent> onInputChanged = command->inputChanged();
                if (!onInputChanged)
                    return;
                isOk = onInputChanged->add(&onInputChangedHandler);
                if (!isOk)
                    return;

                // Get the CommandInputs collection associated with the command.
                Ptr<CommandInputs> inputs = command->commandInputs();
                if (!inputs)
                    return;

                // Create a tab input.
                Ptr<TabCommandInput> tabCmdInput1 = inputs->addTabCommandInput("tab_1", "Tab 1");
                if (!tabCmdInput1)
                    return;
                Ptr<CommandInputs> tab1ChildInputs = tabCmdInput1->children();
                if (!tab1ChildInputs)
                    return;

                // Create a read only textbox input.
                tab1ChildInputs->addTextBoxCommandInput(
                    "readonly_textBox", "Text Box 1", "This is an example of a read-only text box.", 2, true);

                // Create an editable textbox input.
                tab1ChildInputs->addTextBoxCommandInput(
                    "writable_textBox", "Text Box 2", "This is an example of an editable text box.", 2, false);

                // Create a message that spans the entire width of the dialog by leaving out the "name" argument.
                std::string message = "<div align=\"center\">A full width message using <a "
                                      "\"href=\"http:fusion.autodesk.com\">html.</a></div>";
                tab1ChildInputs->addTextBoxCommandInput("fullWidth_textBox", "", message, 1, true);

                // Create a selection input.
                Ptr<SelectionCommandInput> selectionInput =
                    tab1ChildInputs->addSelectionInput("selection", "Select", "Basic select command input");
                if (!selectionInput)
                    return;
                selectionInput->setSelectionLimits(0);

                // Create string value input.
                Ptr<StringValueCommandInput> strInput =
                    tab1ChildInputs->addStringValueInput("string", "Text", "Basic string command input");

                // Create value input.
                tab1ChildInputs->addValueInput("value", "Value", "cm", ValueInput::createByReal(0.0));

                // Create bool value input with checkbox style.
                tab1ChildInputs->addBoolValueInput("checkbox", "Checkbox", true, "", false);

                // Create bool value input with button style that can be clicked.
                tab1ChildInputs->addBoolValueInput("buttonClick", "Click Button", false, "resources/button", true);

                // Create bool value input with button style that has a state.
                tab1ChildInputs->addBoolValueInput("buttonState", "State Button", true, "resources/button", true);

                // Create float slider input with two sliders.
                tab1ChildInputs->addFloatSliderCommandInput("floatSlider", "Float Slider", "cm", 0, 10.0, true);

                // Create float slider input with two sliders and a value list
                std::vector<double> floatValueList;
                floatValueList.push_back(1.0);
                floatValueList.push_back(3.0);
                floatValueList.push_back(4.0);
                floatValueList.push_back(7.0);
                tab1ChildInputs->addFloatSliderListCommandInput("floatSlider2", "Float Slider 2", "cm", floatValueList);

                // Create float slider input with two sliders and visible texts
                Ptr<FloatSliderCommandInput> floatSlider3 =
                    tab1ChildInputs->addFloatSliderCommandInput("floatSlider3", "Float Slider 3", "", 0, 50.0, false);
                if (!floatSlider3)
                    return;
                floatSlider3->setText("Min", "Max");

                // Create integer slider input with one slider
                tab1ChildInputs->addIntegerSliderCommandInput("intSlider", "Integer Slider", 0, 10);

                // Create integer slider input with two sliders and a value list
                std::vector<int> valueList;
                valueList.push_back(1);
                valueList.push_back(3);
                valueList.push_back(4);
                valueList.push_back(7);
                valueList.push_back(11);
                tab1ChildInputs->addIntegerSliderListCommandInput("intSlider2", "Integer Slider 2", valueList);

                // Create float spinner input.
                tab1ChildInputs->addFloatSpinnerCommandInput("spinnerFloat", "Float Spinner", "cm", 0.2, 9.0, 2.2, 1);

                // Create integer spinner input.
                tab1ChildInputs->addIntegerSpinnerCommandInput("spinnerInt", "Integer Spinner", 2, 9, 2, 3);

                // Create dropdown input with checkbox style.
                Ptr<DropDownCommandInput> dropdownInput = tab1ChildInputs->addDropDownCommandInput(
                    "dropdown", "Dropdown 1", DropDownStyles::CheckBoxDropDownStyle);
                if (!dropdownInput)
                    return;
                Ptr<ListItems> dropdownItems = dropdownInput->listItems();
                if (!dropdownItems)
                    return;
                dropdownItems->add("Item 1", false, "resources/One");
                dropdownItems->add("Item 2", false, "resources/Two");

                // Create dropdown input with icon style.
                Ptr<DropDownCommandInput> dropdownInput2 = tab1ChildInputs->addDropDownCommandInput(
                    "dropdown2", "Dropdown 2", DropDownStyles::LabeledIconDropDownStyle);
                if (!dropdownInput2)
                    return;
                Ptr<ListItems> dropdown2Items = dropdownInput2->listItems();
                if (!dropdown2Items)
                    return;
                dropdown2Items->add("Item 1", true, "resources/One");
                dropdown2Items->add("Item 2", false, "resources/Two");

                // Create dropdown input with radio style.
                Ptr<DropDownCommandInput> dropdownInput3 = tab1ChildInputs->addDropDownCommandInput(
                    "dropdown3", "Dropdown 3", DropDownStyles::LabeledIconDropDownStyle);
                if (!dropdownInput3)
                    return;
                Ptr<ListItems> dropdown3Items = dropdownInput3->listItems();
                if (!dropdown3Items)
                    return;
                dropdown3Items->add("Item 1", true, "");
                dropdown3Items->add("Item 2", false, "");

                // Create dropdown input with test list style.
                Ptr<DropDownCommandInput> dropdownInput4 = tab1ChildInputs->addDropDownCommandInput(
                    "dropdown4", "Dropdown 4", DropDownStyles::TextListDropDownStyle);
                if (!dropdownInput4)
                    return;
                Ptr<ListItems> dropdown4Items = dropdownInput4->listItems();
                if (!dropdown4Items)
                    return;
                dropdown4Items->add("Item 1", true, "");
                dropdown4Items->add("Item 2", false, "");

                // Create single selectable button row input.
                Ptr<ButtonRowCommandInput> buttonRowInput =
                    tab1ChildInputs->addButtonRowCommandInput("buttonRow", "Button Row 1", false);
                if (!buttonRowInput)
                    return;
                Ptr<ListItems> buttonRowItems = buttonRowInput->listItems();
                if (!buttonRowItems)
                    return;
                buttonRowItems->add("Item 1", false, "resources/One");
                buttonRowItems->add("Item 2", false, "resources/Two");

                // Create multi selectable button row input.
                Ptr<ButtonRowCommandInput> buttonRowInput2 =
                    tab1ChildInputs->addButtonRowCommandInput("buttonRow2", "Button Row 2", true);
                if (!buttonRowInput2)
                    return;
                Ptr<ListItems> buttonRow2Items = buttonRowInput2->listItems();
                if (!buttonRow2Items)
                    return;
                buttonRow2Items->add("Item 1", false, "resources/One");
                buttonRow2Items->add("Item 2", false, "resources/Two");

                // Create tab input 2.
                Ptr<TabCommandInput> tabCmdInput2 = inputs->addTabCommandInput("tab_2", "Tab 2");
                if (!tabCmdInput2)
                    return;
                Ptr<CommandInputs> tab2ChildInputs = tabCmdInput2->children();
                if (!tab2ChildInputs)
                    return;

                // Create group input.
                Ptr<GroupCommandInput> groupCmdInput = tab2ChildInputs->addGroupCommandInput("group", "Group");
                if (!groupCmdInput)
                    return;
                groupCmdInput->isExpanded(true);
                groupCmdInput->isEnabledCheckBoxDisplayed(true);
                Ptr<CommandInputs> groupChildInputs = groupCmdInput->children();
                if (!groupChildInputs)
                    return;

                // Create radio button group input.
                Ptr<RadioButtonGroupCommandInput> radioButtonGroup =
                    groupChildInputs->addRadioButtonGroupCommandInput("radioButtonGroup", "Radio button group");
                if (!radioButtonGroup)
                    return;
                Ptr<ListItems> radioButtonItems = radioButtonGroup->listItems();
                if (!radioButtonItems)
                    return;
                radioButtonItems->add("Item 1", false);
                radioButtonItems->add("Item 2", false);
                radioButtonItems->add("Item 3", false);

                // Create image input
                Ptr<ImageCommandInput> imageCmdInput =
                    groupChildInputs->addImageCommandInput("image", "Image", "resources/image.png");
                if (!imageCmdInput)
                    return;

                // Create direction input 1.
                Ptr<DirectionCommandInput> directionCmdInput =
                    tab2ChildInputs->addDirectionCommandInput("direction", "Direction");
                if (!directionCmdInput)
                    return;
                directionCmdInput->setManipulator(Point3D::create(0, 0, 0), Vector3D::create(1, 0, 0));

                // Create direction input 2.
                Ptr<DirectionCommandInput> directionCmdInput2 =
                    tab2ChildInputs->addDirectionCommandInput("direction2", "Direction 2", "resources/One");
                if (!directionCmdInput2)
                    return;
                directionCmdInput2->setManipulator(Point3D::create(0, 0, 0), Vector3D::create(0, 1, 0));
                directionCmdInput2->isDirectionFlipped(true);

                // Create distance value input 1.
                Ptr<DistanceValueCommandInput> distanceValueInput = tab2ChildInputs->addDistanceValueCommandInput(
                    "distanceValue", "Distance Value", ValueInput::createByReal(2));
                if (!distanceValueInput)
                    return;
                distanceValueInput->setManipulator(Point3D::create(0, 0, 0), Vector3D::create(1, 0, 0));
                distanceValueInput->minimumValue(0);
                distanceValueInput->isMinimumValueInclusive(true);
                distanceValueInput->maximumValue(10);
                distanceValueInput->isMaximumValueInclusive(true);

                // Create distance value input 2.
                Ptr<DistanceValueCommandInput> distanceValueInput2 = tab2ChildInputs->addDistanceValueCommandInput(
                    "distanceValue2", "DistanceValue 2", ValueInput::createByReal(1));
                if (!distanceValueInput2)
                    return;
                distanceValueInput2->setManipulator(Point3D::create(0, 0, 0), Vector3D::create(0, 1, 0));
                distanceValueInput2->expression("1 in");
                distanceValueInput2->hasMinimumValue(false);
                distanceValueInput2->hasMaximumValue(false);

                // Create table input.
                Ptr<TableCommandInput> tableInput = tab2ChildInputs->addTableCommandInput("table", "Table", 3, "1:1:1");
                addRowToTable(tableInput);

                // Add inputs into the table.
                Ptr<CommandInput> addButtonInput =
                    tab2ChildInputs->addBoolValueInput("tableAdd", "Add", false, "", true);
                tableInput->addToolbarCommandInput(addButtonInput);
                Ptr<CommandInput> deleteButtonInput =
                    tab2ChildInputs->addBoolValueInput("tableDelete", "Delete", false, "", true);
                tableInput->addToolbarCommandInput(deleteButtonInput);

                // Create angle value input.
                Ptr<AngleValueCommandInput> angleValueInput = tab2ChildInputs->addAngleValueCommandInput(
                    "angleValue", "AngleValue", ValueInput::createByString("30 degree"));
                angleValueInput->setManipulator(
                    Point3D::create(0, 0, 0), Vector3D::create(1, 0, 0), Vector3D::create(0, 0, 1));
                angleValueInput->hasMinimumValue(false);
                angleValueInput->hasMaximumValue(false);

                // Create tab inputs 3
                Ptr<TabCommandInput> tabCmdInput3 = inputs->addTabCommandInput("tab_3", "Tab 3");
                if (!tabCmdInput3)
                    return;
                Ptr<CommandInputs> tab3ChildInputs = tabCmdInput3->children();
                if (!tab3ChildInputs)
                    return;
                // Create group
                Ptr<GroupCommandInput> sliderGroup =
                    tab3ChildInputs->addGroupCommandInput("slider_configuration", "Configuration");
                if (!sliderGroup)
                {
                    return;
                }
                Ptr<CommandInputs> sliderInputs = sliderGroup->children();
                // Create integer spinner input
                sliderInputs->addIntegerSpinnerCommandInput("slider_controller", "Num sliders", 1, 5, 1, 1);
                if (!sliderInputs)
                {
                    return;
                }
                updateSliders(sliderInputs);
            }
        }
    }

  private:
    OnExecuteEventHander onExecuteHandler;
    OnDestroyEventHandler onDestroyHandler;
    OnInputChangedEventHander onInputChangedHandler;
} _cmdCreatedHandler;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    // Create the command definition.
    Ptr<CommandDefinitions> commandDefinitions = ui->commandDefinitions();
    if (!commandDefinitions)
        return nullptr;

    // Get the existing command definition or create it if it doesn't already exist.
    Ptr<CommandDefinition> cmdDef = commandDefinitions->itemById("cmdInputsSample");
    if (!cmdDef)
    {
        cmdDef = commandDefinitions->addButtonDefinition(
            "cmdInputsSample", "Command Inputs Sample", "Sample to demonstrate various command inputs.");
    }

    // Connect to the command created event.
    Ptr<CommandCreatedEvent> commandCreatedEvent = cmdDef->commandCreated();
    if (!commandCreatedEvent)
        return false;
    commandCreatedEvent->add(&_cmdCreatedHandler);

    // Execute the command definition.
    cmdDef->execute();

    // Prevent this module from being terminated when the script returns, because we are waiting for event handlers to
    // fire.
    adsk::autoTerminate(false);

    return true;
}
```

|  |
| --- |
| Copy Code |

```
#Author-Autodesk Inc.
#Description-Demo command input examples
import adsk.core, adsk.fusion, traceback

_app = None
_ui  = None
_rowNumber = 0

# Global set of event handlers to keep them referenced for the duration of the command
_handlers = []

# Adds a new row to the table.
def addRowToTable(tableInput):
    global _rowNumber
    # Get the CommandInputs object associated with the parent command.
    cmdInputs = adsk.core.CommandInputs.cast(tableInput.commandInputs)

    # Create three new command inputs.
    valueInput = cmdInputs.addValueInput('TableInput_value{}'.format(_rowNumber), 'Value', 'cm', adsk.core.ValueInput.createByReal(_rowNumber))
    stringInput =  cmdInputs.addStringValueInput('TableInput_string{}'.format(_rowNumber), 'String', str(_rowNumber))
    spinnerInput = cmdInputs.addIntegerSpinnerCommandInput('spinnerInt{}'.format(_rowNumber), 'Integer Spinner', 0 , 100 , 2, int(_rowNumber))

    # Add the inputs to the table.
    row = tableInput.rowCount
    tableInput.addCommandInput(valueInput, row, 0)
    tableInput.addCommandInput(stringInput, row, 1)
    tableInput.addCommandInput(spinnerInput, row, 2)

    # Increment a counter used to make each row unique.
    _rowNumber = _rowNumber + 1

def updateSliders(sliderInputs):
    """
    Populate 'slider_configuration' group with as many sliders as set in 'slider_controller'.
    Delete previous ones and create new sliders.
    """
    spinner = sliderInputs.itemById("slider_controller")
    value = spinner.value
    # check ranges
    if value > spinner.maximumValue or value < spinner.minimumValue:
        return

    # delete all sliders we have
    toRemove = []
    for i in range(sliderInputs.count):
        input = sliderInputs.item(i)
        if input.objectType == adsk.core.FloatSliderCommandInput.classType():
            toRemove.append(input)

    for input in toRemove:
        input.deleteMe()

    # create new ones with range depending on total number
    for i in range(1, value+1):
        id = str(i)
        sliderInputs.addFloatSliderCommandInput("slider_configuration_" + id, "slider_" + id, "cm", 0, 10.0*value)

# Event handler that reacts to any changes the user makes to any of the command inputs.
class MyCommandInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            eventArgs = adsk.core.InputChangedEventArgs.cast(args)
            inputs = eventArgs.inputs
            cmdInput = eventArgs.input
            # onInputChange for slider controller
            if cmdInput.id == "slider_controller":
                sliderGroup = adsk.core.GroupCommandInput.cast(cmdInput.parentCommandInput)
                sliderInputs = sliderGroup.children
                updateSliders(sliderInputs)
            else:
                tableInput = inputs.itemById('table')
                if cmdInput.id == 'tableAdd':
                    addRowToTable(tableInput)
                elif cmdInput.id == 'tableDelete':
                    if tableInput.selectedRow == -1:
                        _ui.messageBox('Select one row to delete.')
                    else:
                        tableInput.deleteRow(tableInput.selectedRow)

        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Event handler that reacts to when the command is destroyed. This terminates the script.
class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # When the command is done, terminate the script
            # This will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Event handler that reacts when the command definitio is executed which
# results in the command being created and this event being fired.
class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # Get the command that was created.
            cmd = adsk.core.Command.cast(args.command)

            # Connect to the command destroyed event.
            onDestroy = MyCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            _handlers.append(onDestroy)

            # Connect to the input changed event.
            onInputChanged = MyCommandInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            _handlers.append(onInputChanged)

            # Get the CommandInputs collection associated with the command.
            inputs = cmd.commandInputs

            # Create a tab input.
            tabCmdInput1 = inputs.addTabCommandInput('tab_1', 'Tab 1')
            tab1ChildInputs = tabCmdInput1.children

            # Create a read only textbox input.
            tab1ChildInputs.addTextBoxCommandInput('readonly_textBox', 'Text Box 1', 'This is an example of a read-only text box.', 2, True)

            # Create an editable textbox input.
            tab1ChildInputs.addTextBoxCommandInput('writable_textBox', 'Text Box 2', 'This is an example of an editable text box.', 2, False)

            # Create a message that spans the entire width of the dialog by leaving out the "name" argument.
            message = '<div align="center">A "full width" message using <a href="http:fusion.autodesk.com">html.</a></div>'
            tab1ChildInputs.addTextBoxCommandInput('fullWidth_textBox', '', message, 1, True)

            # Create a selection input.
            selectionInput = tab1ChildInputs.addSelectionInput('selection', 'Select', 'Basic select command input')
            selectionInput.setSelectionLimits(0)

            # Create a string value input.
            strInput = tab1ChildInputs.addStringValueInput('string', 'Text', 'Basic string command input')

            # Create value input.
            tab1ChildInputs.addValueInput('value', 'Value', 'cm', adsk.core.ValueInput.createByReal(0.0))

            # Create bool value input with checkbox style.
            tab1ChildInputs.addBoolValueInput('checkbox', 'Checkbox', True, '', False)

            # Create bool value input with button style that can be clicked.
            tab1ChildInputs.addBoolValueInput('buttonClick', 'Click Button', False, 'resources/button', True)

            # Create bool value input with button style that has a state.
            tab1ChildInputs.addBoolValueInput('buttonState', 'State Button', True, 'resources/button', True)

            # Create float slider input with two sliders.
            tab1ChildInputs.addFloatSliderCommandInput('floatSlider', 'Float Slider', 'cm', 0, 10.0, True)

            # Create float slider input with two sliders and a value list.
            floatValueList = [1.0, 3.0, 4.0, 7.0]
            tab1ChildInputs.addFloatSliderListCommandInput('floatSlider2', 'Float Slider 2', 'cm', floatValueList)

            # Create float slider input with two sliders and visible texts.
            floatSlider3 = tab1ChildInputs.addFloatSliderCommandInput('floatSlider3', 'Float Slider 3', '', 0, 50.0, False)
            floatSlider3.setText('Min', 'Max')

            # Create integer slider input with one slider.
            tab1ChildInputs.addIntegerSliderCommandInput('intSlider', 'Integer Slider', 0, 10);
            valueList = [1, 3, 4, 7, 11]

            # Create integer slider input with two sliders and a value list.
            tab1ChildInputs.addIntegerSliderListCommandInput('intSlider2', 'Integer Slider 2', valueList)

            # Create float spinner input.
            tab1ChildInputs.addFloatSpinnerCommandInput('spinnerFloat', 'Float Spinner', 'cm', 0.2 , 9.0 , 2.2, 1)

            # Create integer spinner input.
            tab1ChildInputs.addIntegerSpinnerCommandInput('spinnerInt', 'Integer Spinner', 2 , 9 , 2, 3)

            # Create dropdown input with checkbox style.
            dropdownInput = tab1ChildInputs.addDropDownCommandInput('dropdown', 'Dropdown 1', adsk.core.DropDownStyles.CheckBoxDropDownStyle)
            dropdownItems = dropdownInput.listItems
            dropdownItems.add('Item 1', False, 'resources/One')
            dropdownItems.add('Item 2', False, 'resources/Two')

            # Create dropdown input with icon style.
            dropdownInput2 = tab1ChildInputs.addDropDownCommandInput('dropdown2', 'Dropdown 2', adsk.core.DropDownStyles.LabeledIconDropDownStyle);
            dropdown2Items = dropdownInput2.listItems
            dropdown2Items.add('Item 1', True, 'resources/One')
            dropdown2Items.add('Item 2', False, 'resources/Two')

            # Create dropdown input with radio style.
            dropdownInput3 = tab1ChildInputs.addDropDownCommandInput('dropdown3', 'Dropdown 3', adsk.core.DropDownStyles.LabeledIconDropDownStyle);
            dropdown3Items = dropdownInput3.listItems
            dropdown3Items.add('Item 1', True, '')
            dropdown3Items.add('Item 2', False, '')

            # Create dropdown input with test list style.
            dropdownInput4 = tab1ChildInputs.addDropDownCommandInput('dropdown4', 'Dropdown 4', adsk.core.DropDownStyles.TextListDropDownStyle);
            dropdown4Items = dropdownInput4.listItems
            dropdown4Items.add('Item 1', True, '')
            dropdown4Items.add('Item 2', False, '')

            # Create single selectable button row input.
            buttonRowInput = tab1ChildInputs.addButtonRowCommandInput('buttonRow', 'Single Select Buttons', False)
            buttonRowInput.listItems.add('Item 1', False, 'resources/One')
            buttonRowInput.listItems.add('Item 2', False, 'resources/Two')

            # Create multi selectable button row input.
            buttonRowInput2 = tab1ChildInputs.addButtonRowCommandInput('buttonRow2', 'Multi-select Buttons', True)
            buttonRowInput2.listItems.add('Item 1', False, 'resources/One')
            buttonRowInput2.listItems.add('Item 2', False, 'resources/Two')

            # Create tab input 2
            tabCmdInput2 = inputs.addTabCommandInput('tab_2', 'Tab 2')
            tab2ChildInputs = tabCmdInput2.children

            # Create group input.
            groupCmdInput = tab2ChildInputs.addGroupCommandInput('group', 'Group')
            groupCmdInput.isExpanded = True
            groupCmdInput.isEnabledCheckBoxDisplayed = True
            groupChildInputs = groupCmdInput.children

            # Create radio button group input.
            radioButtonGroup = groupChildInputs.addRadioButtonGroupCommandInput('radioButtonGroup', 'Radio button group')
            radioButtonItems = radioButtonGroup.listItems
            radioButtonItems.add("Item 1", False)
            radioButtonItems.add("Item 2", False)
            radioButtonItems.add("Item 3", False)

            # Create image input.
            groupChildInputs.addImageCommandInput('image', 'Image', "resources/image.png")

            # Create direction input 1.
            directionCmdInput = tab2ChildInputs.addDirectionCommandInput('direction', 'Direction1')
            directionCmdInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))

            # Create direction input 2.
            directionCmdInput2 = tab2ChildInputs.addDirectionCommandInput('direction2', 'Direction 2', 'resources/One')
            directionCmdInput2.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(0, 1, 0))
            directionCmdInput2.isDirectionFlipped = True

            # Create distance value input 1.
            distanceValueInput = tab2ChildInputs.addDistanceValueCommandInput('distanceValue', 'DistanceValue', adsk.core.ValueInput.createByReal(2))
            distanceValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
            distanceValueInput.minimumValue = 0
            distanceValueInput.isMinimumValueInclusive = True
            distanceValueInput.maximumValue = 10
            distanceValueInput.isMaximumValueInclusive = True

            # Create distance value input 2.
            distanceValueInput2 = tab2ChildInputs.addDistanceValueCommandInput('distanceValue2', 'DistanceValue 2', adsk.core.ValueInput.createByReal(1))
            distanceValueInput2.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(0, 1, 0))
            distanceValueInput2.expression = '1 in'
            distanceValueInput2.hasMinimumValue = False
            distanceValueInput2.hasMaximumValue = False

            # Create table input
            tableInput = tab2ChildInputs.addTableCommandInput('table', 'Table', 3, '1:1:1')
            addRowToTable(tableInput)

            # Add inputs into the table.
            addButtonInput = tab2ChildInputs.addBoolValueInput('tableAdd', 'Add', False, '', True)
            tableInput.addToolbarCommandInput(addButtonInput)
            deleteButtonInput = tab2ChildInputs.addBoolValueInput('tableDelete', 'Delete', False, '', True)
            tableInput.addToolbarCommandInput(deleteButtonInput)

            # Create angle value input.
            angleValueInput = tab2ChildInputs.addAngleValueCommandInput('angleValue', 'AngleValue', adsk.core.ValueInput.createByString('30 degree'))
            angleValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 0, 1))
            angleValueInput.hasMinimumValue = False
            angleValueInput.hasMaximumValue = False

            # Create tab input 3
            tabCmdInput3 = inputs.addTabCommandInput('tab_3', 'Tab 3')
            tab3ChildInputs = tabCmdInput3.children
            # Create group
            sliderGroup = tab3ChildInputs.addGroupCommandInput("slider_configuration", "Configuration")
            sliderInputs = sliderGroup.children
            # Create integer spinner input
            sliderInputs.addIntegerSpinnerCommandInput("slider_controller", "Num sliders", 1, 5, 1, 1)
            updateSliders(sliderInputs)
        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run(context):
    try:
        global _app, _ui
        _app = adsk.core.Application.get()
        _ui = _app.userInterface

        # Get the existing command definition or create it if it doesn't already exist.
        cmdDef = _ui.commandDefinitions.itemById('cmdInputsSample')
        if not cmdDef:
            cmdDef = _ui.commandDefinitions.addButtonDefinition('cmdInputsSample', 'Command Inputs Sample', 'Sample to demonstrate various command inputs.')

        # Connect to the command created event.
        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        _handlers.append(onCommandCreated)

        # Execute the command definition.
        cmdDef.execute()

        # Prevent this module from being terminated when the script returns, because we are waiting for event handlers to fire.
        adsk.autoTerminate(False)
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |