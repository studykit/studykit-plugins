# TextBoxCommandInput Object

Derived from: [CommandInput](CommandInput.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextBoxCommandInput.h>

## Description

Provides a command input to interact with a text box.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TextBoxCommandInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](TextBoxCommandInput_deleteMe.htm) | Deletes this Command input. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [commandInputs](TextBoxCommandInput_commandInputs.htm) | Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput. |
| [formattedText](TextBoxCommandInput_formattedText.htm) | Gets and sets the formatted text displayed in the dialog. |
| [id](TextBoxCommandInput_id.htm) | Gets the unique identifier for this input in the command's CommandInputs. |
| [isEnabled](TextBoxCommandInput_isEnabled.htm) | Gets or sets if this input is currently enabled or disabled for user interaction. |
| [isFullWidth](TextBoxCommandInput_isFullWidth.htm) | Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs. |
| [isReadOnly](TextBoxCommandInput_isReadOnly.htm) | Gets and sets if the text box is read-only or not. If it is read-only the user cannot edit the text. |
| [isValid](TextBoxCommandInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](TextBoxCommandInput_isVisible.htm) | Gets or sets if this input will be visible to the user.   Setting a SelectionCommandInput to be invisible will clear any selections it currently has. |
| [name](TextBoxCommandInput_name.htm) | Gets the user visible name of this input. |
| [numRows](TextBoxCommandInput_numRows.htm) | Gets and sets the height of the text box as defined by the number of rows of text that can be displayed. If the text is larger than will fit in the box a scroll bar will automatically be displayed. |
| [objectType](TextBoxCommandInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentCommand](TextBoxCommandInput_parentCommand.htm) | Gets the parent Command. |
| [parentCommandInput](TextBoxCommandInput_parentCommandInput.htm) | Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent. |
| [text](TextBoxCommandInput_text.htm) | Gets and sets the text in the text box. When text is set using the text property, any HTML formatting is ignored and the full string will be displayed in the text box. For example, if you specify the string "Here is a <b>Bold</b> word", and use the formattedText property, you will see "Here is a **Bold** word" in the text box. However, if you use the text property, you will see "Here is a <b>Bold</b> word" and when you get the text property you will get back "Here is a <b>Bold</b> word". This can be useful if you're using the text box to have the user enter HTML code so it's treated as a simple string. |
| [toolClipFilename](TextBoxCommandInput_toolClipFilename.htm) | Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |
| [tooltip](TextBoxCommandInput_tooltip.htm) | Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control. |
| [tooltipDescription](TextBoxCommandInput_tooltipDescription.htm) | Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |

## Accessed From

[CommandInputs.addTextBoxCommandInput](CommandInputs_addTextBoxCommandInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |