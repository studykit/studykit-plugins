# StatusMessages Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessages.h>

## Description

A collection of status messages associated with a Status object. The primary purpose of the messages is to describe the reason for a warning or failure and display the messages in the alert dialog.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addError](StatusMessages_addError.htm) | Adds a new error status message to the list of warning and error messages. |
| [addWarning](StatusMessages_addWarning.htm) | Adds a new warning status message to the list of warning and error messages. |
| [classType](StatusMessages_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](StatusMessages_item.htm) | Returns the specified status message using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](StatusMessages_count.htm) | Returns the number of status messages in this collection. |
| [isValid](StatusMessages_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](StatusMessages_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Status.statusMessages](Status_statusMessages.htm), [StatusMessage.childStatusMessages](StatusMessage_childStatusMessages.htm)

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |