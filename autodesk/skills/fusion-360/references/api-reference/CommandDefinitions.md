# CommandDefinitions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinitions.h>

## Description

Provides access to all of the available command definitions. This is all those created via the API but also includes the command definitions defined by Fusion for the native commands.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addButtonDefinition](CommandDefinitions_addButtonDefinition.htm) | Creates a new command definition that can be used to create a button control and handle the response when the button is clicked. |
| [addCheckBoxDefinition](CommandDefinitions_addCheckBoxDefinition.htm) | Creates a new command definition that can be used to create a single check box control and handle the response when the check box is clicked. |
| [addListDefinition](CommandDefinitions_addListDefinition.htm) | Creates a new command definition that can be used to create a list of check boxes, radio buttons, or text with an icon within a pop-up. |
| [classType](CommandDefinitions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CommandDefinitions_item.htm) | Returns the CommandDefinition at the specified index. |
| [itemById](CommandDefinitions_itemById.htm) | Returns the CommandDefinition that has the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CommandDefinitions_count.htm) | Gets the number of command definitions. |
| [isValid](CommandDefinitions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CommandDefinitions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[UserInterface.commandDefinitions](UserInterface_commandDefinitions.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |