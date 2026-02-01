# CommandInputs Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInputs.h>

## Description

Provides access to the set of inputs for a command. Command inputs are used to gather inputs from the user when a command is executed. The set of inputs used by a command are created and added to the command with the methods in this class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addAngleValueCommandInput](CommandInputs_addAngleValueCommandInput.htm) | Adds a new angle value input to the command. This displays a field in the command dialog where an angle value can be entered. It displays the angle in the dialog using degrees. There is also a graphical manipulator associated with the input to allow the user to graphically set the value. You use the setManipulator method of the returned AngleValueCommandInput object to define the position and orientation of the manipulator. |
| [addBoolValueInput](CommandInputs_addBoolValueInput.htm) | Adds a new boolean input to the command. The input can be shown as a check box or a button. If it's a button you need to specify the resource folder to define the icon to use. Buttons don't have an up or down state but can just be clicked. |
| [addBrowserCommandInput](CommandInputs_addBrowserCommandInput.htm) | Adds a new command input to the command that behaves as a browser. |
| [addButtonRowCommandInput](CommandInputs_addButtonRowCommandInput.htm) | Adds a new row of buttons as a command input. Depending on the isMultiSelectEnabled argument it can act like an option list where only a single button on the row can be selected at a time or multiple buttons can be selected. The buttons are defined by using the returned ButtonRowCommandInput object. |
| [addDirectionCommandInput](CommandInputs_addDirectionCommandInput.htm) | Adds a new direction command input to the command. The input can be shown as a check box or a button. If it's a button you need to specify the resource folder to define the icon to use for the Button. |
| [addDistanceValueCommandInput](CommandInputs_addDistanceValueCommandInput.htm) | Adds a new distance value input to the command. This displays a field in the command dialog where a distance value can be entered. It displays the distance in the dialog using current document default unit. There is also a graphical manipulator associated with the input. You use the setManipulator method of the returned DistanceValueCommandInput object to define the position and orientation of the manipulator. |
| [addDropDownCommandInput](CommandInputs_addDropDownCommandInput.htm) | Adds a new empty drop-down input to the command. drop-downs of various types are supported. To add items to the drop down use the returned DropDownCommandInput object. |
| [addFloatSliderCommandInput](CommandInputs_addFloatSliderCommandInput.htm) | Adds a new slider input to the command. The value type is double. |
| [addFloatSliderListCommandInput](CommandInputs_addFloatSliderListCommandInput.htm) | Adds a new slider input to the command. The value type is float. |
| [addFloatSpinnerCommandInput](CommandInputs_addFloatSpinnerCommandInput.htm) | Adds a new spinner input to the command. The value type is float. |
| [addGroupCommandInput](CommandInputs_addGroupCommandInput.htm) | Adds a new Group input to the command. Group Command inputs organize a set of command inputs into a collapsible list within a command dialog. |
| [addImageCommandInput](CommandInputs_addImageCommandInput.htm) | Adds a new Image input to the command. |
| [addIntegerSliderCommandInput](CommandInputs_addIntegerSliderCommandInput.htm) | Adds a new slider input to the command. The value type is integer. |
| [addIntegerSliderListCommandInput](CommandInputs_addIntegerSliderListCommandInput.htm) | Adds a new slider input to the command. The value type is integer. |
| [addIntegerSpinnerCommandInput](CommandInputs_addIntegerSpinnerCommandInput.htm) | Adds a new spinner input to the command. The value type is integer. |
| [addRadioButtonGroupCommandInput](CommandInputs_addRadioButtonGroupCommandInput.htm) | Adds a new Radio Button Group input to the command. |
| [addSelectionInput](CommandInputs_addSelectionInput.htm) | Adds a new selection input to the command. This allows you to get entity selections from the user. The default behavior is that only one entity can be selected and it can be of any type. To change the selection behavior to select specific types and control the number of items selected use the methods and properties on the returned SelectionCommandInput object. You can also use the selectionEvent event that's associated with the command to have additional control over the selection process. |
| [addSeparatorCommandInput](CommandInputs_addSeparatorCommandInput.htm) | Adds a new Separator input to the command. A separator input is for visual purposes only and creates a line in the dialog providing a visual separation between the command inputs above and below where the separator is inserted. |
| [addStringValueInput](CommandInputs_addStringValueInput.htm) | Adds a new string input to the command. |
| [addTabCommandInput](CommandInputs_addTabCommandInput.htm) | Adds a new Tab input to the command. Tab command inputs contain a set of command inputs and/or group command inputs |
| [addTableCommandInput](CommandInputs_addTableCommandInput.htm) | Adds a new table command input to the command. |
| [addTextBoxCommandInput](CommandInputs_addTextBoxCommandInput.htm) | Adds a text box input to the command. |
| [addTriadCommandInput](CommandInputs_addTriadCommandInput.htm) | Adds a new triad command input to the command. The input is initially invisible to allow you to define the desired behavior and then set the isVisible property to true when you're ready to display the triad. |
| [addValueInput](CommandInputs_addValueInput.htm) | Adds a new value input to the command. |
| [classType](CommandInputs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CommandInputs_item.htm) | Returns the specified command input using an index into the collection. |
| [itemById](CommandInputs_itemById.htm) | Returns the command input that has the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [command](CommandInputs_command.htm) | Gets the parent Command object. |
| [count](CommandInputs_count.htm) | Gets the number of inputs. |
| [isValid](CommandInputs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CommandInputs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[AngleValueCommandInput.commandInputs](AngleValueCommandInput_commandInputs.htm), [BoolValueCommandInput.commandInputs](BoolValueCommandInput_commandInputs.htm), [BrowserCommandInput.commandInputs](BrowserCommandInput_commandInputs.htm), [ButtonRowCommandInput.commandInputs](ButtonRowCommandInput_commandInputs.htm), [Command.commandInputs](Command_commandInputs.htm), [CommandInput.commandInputs](CommandInput_commandInputs.htm), [DirectionCommandInput.commandInputs](DirectionCommandInput_commandInputs.htm), [DistanceValueCommandInput.commandInputs](DistanceValueCommandInput_commandInputs.htm), [DropDownCommandInput.commandInputs](DropDownCommandInput_commandInputs.htm), [FloatSliderCommandInput.commandInputs](FloatSliderCommandInput_commandInputs.htm), [FloatSpinnerCommandInput.commandInputs](FloatSpinnerCommandInput_commandInputs.htm), [GroupCommandInput.children](GroupCommandInput_children.htm), [GroupCommandInput.commandInputs](GroupCommandInput_commandInputs.htm), [ImageCommandInput.commandInputs](ImageCommandInput_commandInputs.htm), [InputChangedEventArgs.inputs](InputChangedEventArgs_inputs.htm), [IntegerSliderCommandInput.commandInputs](IntegerSliderCommandInput_commandInputs.htm), [IntegerSpinnerCommandInput.commandInputs](IntegerSpinnerCommandInput_commandInputs.htm), [RadioButtonGroupCommandInput.commandInputs](RadioButtonGroupCommandInput_commandInputs.htm), [SelectionCommandInput.commandInputs](SelectionCommandInput_commandInputs.htm), [SeparatorCommandInput.commandInputs](SeparatorCommandInput_commandInputs.htm), [SliderCommandInput.commandInputs](SliderCommandInput_commandInputs.htm), [StringValueCommandInput.commandInputs](StringValueCommandInput_commandInputs.htm), [TabCommandInput.children](TabCommandInput_children.htm), [TabCommandInput.commandInputs](TabCommandInput_commandInputs.htm), [TableCommandInput.commandInputs](TableCommandInput_commandInputs.htm), [TextBoxCommandInput.commandInputs](TextBoxCommandInput_commandInputs.htm), [TriadCommandInput.commandInputs](TriadCommandInput_commandInputs.htm), [ValidateInputsEventArgs.inputs](ValidateInputsEventArgs_inputs.htm), [ValueCommandInput.commandInputs](ValueCommandInput_commandInputs.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |