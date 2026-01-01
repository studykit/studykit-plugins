# CommandInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInput.h>

## Description

The base class for all command inputs. A CommandInput is used to gather an input value from the user when a command is executed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CommandInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](CommandInput_deleteMe.htm) | Deletes this Command input. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [commandInputs](CommandInput_commandInputs.htm) | Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput. |
| [id](CommandInput_id.htm) | Gets the unique identifier for this input in the command's CommandInputs. |
| [isEnabled](CommandInput_isEnabled.htm) | Gets or sets if this input is currently enabled or disabled for user interaction. |
| [isFullWidth](CommandInput_isFullWidth.htm) | Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs. |
| [isValid](CommandInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](CommandInput_isVisible.htm) | Gets or sets if this input will be visible to the user.   Setting a SelectionCommandInput to be invisible will clear any selections it currently has. |
| [name](CommandInput_name.htm) | Gets the user visible name of this input. |
| [objectType](CommandInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentCommand](CommandInput_parentCommand.htm) | Gets the parent Command. |
| [parentCommandInput](CommandInput_parentCommandInput.htm) | Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent. |
| [toolClipFilename](CommandInput_toolClipFilename.htm) | Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |
| [tooltip](CommandInput_tooltip.htm) | Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control. |
| [tooltipDescription](CommandInput_tooltipDescription.htm) | Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |

## Accessed From

[AngleValueCommandInput.parentCommandInput](AngleValueCommandInput_parentCommandInput.htm), [BoolValueCommandInput.parentCommandInput](BoolValueCommandInput_parentCommandInput.htm), [BrowserCommandInput.parentCommandInput](BrowserCommandInput_parentCommandInput.htm), [ButtonRowCommandInput.parentCommandInput](ButtonRowCommandInput_parentCommandInput.htm), [CommandInput.parentCommandInput](CommandInput_parentCommandInput.htm), [CommandInputs.item](CommandInputs_item.htm), [CommandInputs.itemById](CommandInputs_itemById.htm), [DirectionCommandInput.parentCommandInput](DirectionCommandInput_parentCommandInput.htm), [DistanceValueCommandInput.parentCommandInput](DistanceValueCommandInput_parentCommandInput.htm), [DropDownCommandInput.parentCommandInput](DropDownCommandInput_parentCommandInput.htm), [FloatSliderCommandInput.parentCommandInput](FloatSliderCommandInput_parentCommandInput.htm), [FloatSpinnerCommandInput.parentCommandInput](FloatSpinnerCommandInput_parentCommandInput.htm), [GroupCommandInput.parentCommandInput](GroupCommandInput_parentCommandInput.htm), [ImageCommandInput.parentCommandInput](ImageCommandInput_parentCommandInput.htm), [InputChangedEventArgs.input](InputChangedEventArgs_input.htm), [IntegerSliderCommandInput.parentCommandInput](IntegerSliderCommandInput_parentCommandInput.htm), [IntegerSpinnerCommandInput.parentCommandInput](IntegerSpinnerCommandInput_parentCommandInput.htm), [RadioButtonGroupCommandInput.parentCommandInput](RadioButtonGroupCommandInput_parentCommandInput.htm), [SelectionCommandInput.parentCommandInput](SelectionCommandInput_parentCommandInput.htm), [SeparatorCommandInput.parentCommandInput](SeparatorCommandInput_parentCommandInput.htm), [SliderCommandInput.parentCommandInput](SliderCommandInput_parentCommandInput.htm), [StringValueCommandInput.parentCommandInput](StringValueCommandInput_parentCommandInput.htm), [TabCommandInput.parentCommandInput](TabCommandInput_parentCommandInput.htm), [TableCommandInput.getInputAtPosition](TableCommandInput_getInputAtPosition.htm), [TableCommandInput.parentCommandInput](TableCommandInput_parentCommandInput.htm), [TextBoxCommandInput.parentCommandInput](TextBoxCommandInput_parentCommandInput.htm), [TriadCommandInput.parentCommandInput](TriadCommandInput_parentCommandInput.htm), [ValueCommandInput.parentCommandInput](ValueCommandInput_parentCommandInput.htm)

## Derived Classes

[AngleValueCommandInput](AngleValueCommandInput.htm), [BoolValueCommandInput](BoolValueCommandInput.htm), [BrowserCommandInput](BrowserCommandInput.htm), [ButtonRowCommandInput](ButtonRowCommandInput.htm), [DirectionCommandInput](DirectionCommandInput.htm), [DistanceValueCommandInput](DistanceValueCommandInput.htm), [DropDownCommandInput](DropDownCommandInput.htm), [FloatSpinnerCommandInput](FloatSpinnerCommandInput.htm), [GroupCommandInput](GroupCommandInput.htm), [ImageCommandInput](ImageCommandInput.htm), [IntegerSpinnerCommandInput](IntegerSpinnerCommandInput.htm), [RadioButtonGroupCommandInput](RadioButtonGroupCommandInput.htm), [SelectionCommandInput](SelectionCommandInput.htm), [SeparatorCommandInput](SeparatorCommandInput.htm), [SliderCommandInput](SliderCommandInput.htm), [StringValueCommandInput](StringValueCommandInput.htm), [TabCommandInput](TabCommandInput.htm), [TableCommandInput](TableCommandInput.htm), [TextBoxCommandInput](TextBoxCommandInput.htm), [TriadCommandInput](TriadCommandInput.htm), [ValueCommandInput](ValueCommandInput.htm)

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