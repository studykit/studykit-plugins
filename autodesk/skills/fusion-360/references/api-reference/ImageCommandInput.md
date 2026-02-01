# ImageCommandInput Object

Derived from: [CommandInput](CommandInput.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ImageCommandInput.h>

## Description

Provides an image command input for including an image in a command dialog.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ImageCommandInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ImageCommandInput_deleteMe.htm) | Deletes this Command input. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [commandInputs](ImageCommandInput_commandInputs.htm) | Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput. |
| [id](ImageCommandInput_id.htm) | Gets the unique identifier for this input in the command's CommandInputs. |
| [imageFile](ImageCommandInput_imageFile.htm) | Gets and sets the full path and file name of the image file. Supported image format is .png Images are displayed in the command dialog using their actual size. |
| [isEnabled](ImageCommandInput_isEnabled.htm) | Gets or sets if this input is currently enabled or disabled for user interaction. |
| [isFullWidth](ImageCommandInput_isFullWidth.htm) | Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs. |
| [isValid](ImageCommandInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](ImageCommandInput_isVisible.htm) | Gets or sets if this input will be visible to the user.   Setting a SelectionCommandInput to be invisible will clear any selections it currently has. |
| [name](ImageCommandInput_name.htm) | Gets the user visible name of this input. |
| [objectType](ImageCommandInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentCommand](ImageCommandInput_parentCommand.htm) | Gets the parent Command. |
| [parentCommandInput](ImageCommandInput_parentCommandInput.htm) | Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent. |
| [scaleFactor](ImageCommandInput_scaleFactor.htm) | Gets and sets the scale of the image. This defaults to 1.0, which is full-scale. |
| [toolClipFilename](ImageCommandInput_toolClipFilename.htm) | Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |
| [tooltip](ImageCommandInput_tooltip.htm) | Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control. |
| [tooltipDescription](ImageCommandInput_tooltipDescription.htm) | Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text. |

## Accessed From

[CommandInputs.addImageCommandInput](CommandInputs_addImageCommandInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |