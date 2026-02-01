# SeparatorCommandInput Object

Derived from: [CommandInput](CommandInput.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorCommandInput.h>

## Description

An object that represents a visual separator within a command dialog.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SeparatorCommandInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](SeparatorCommandInput_deleteMe.htm) | Deletes this Command input. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [commandInputs](SeparatorCommandInput_commandInputs.htm) | Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput. |
| [id](SeparatorCommandInput_id.htm) | Gets the unique identifier for this input in the command's CommandInputs. |
| [isEnabled](SeparatorCommandInput_isEnabled.htm) | Gets or sets if this input is currently enabled or disabled for user interaction. |
| [isFullWidth](SeparatorCommandInput_isFullWidth.htm) | Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs. |
| [isValid](SeparatorCommandInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SeparatorCommandInput_isVisible.htm) | Gets or sets if this input will be visible to the user.   Setting a SelectionCommandInput to be invisible will clear any selections it currently has. |
| [name](SeparatorCommandInput_name.htm) | Gets the user visible name of this input. |
| [objectType](SeparatorCommandInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentCommand](SeparatorCommandInput_parentCommand.htm) | Gets the parent Command. |
| [parentCommandInput](SeparatorCommandInput_parentCommandInput.htm) | Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent. |
| [toolClipFilename](SeparatorCommandInput_toolClipFilename.htm) | Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |
| [tooltip](SeparatorCommandInput_tooltip.htm) | Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control. |
| [tooltipDescription](SeparatorCommandInput_tooltipDescription.htm) | Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |

## Accessed From

[CommandInputs.addSeparatorCommandInput](CommandInputs_addSeparatorCommandInput.htm)

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |