# ValidateInputsEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventArgs.h>

## Description

Provides a set of arguments from a firing ValidateInputsEvent to a ValidateInputsEventHandler's notify callback method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ValidateInputsEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [areInputsValid](ValidateInputsEventArgs_areInputsValid.htm) | Used with AreInputsValid event to specify if the all of the inputs for the command are valid or not. If you set this to false, indicating they are not valid, the OK button for the dialog is disabled forcing the user to correct the inputs before continuing. If you set this to true the OK button will be enabled, as long as the inputs satisfy their own requirements. For example, if a SelectionCommandInput is defined to have at minimum number of entities selected, that requirement must be met, or if a ValueCommandInput has an invalid value specified, the OK button will still be disabled. |
| [firingEvent](ValidateInputsEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [inputs](ValidateInputsEventArgs_inputs.htm) | Returns the collection of command inputs that are associated with the command this event is being fired for. |
| [isValid](ValidateInputsEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ValidateInputsEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |