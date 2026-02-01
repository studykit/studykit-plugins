# DataEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventArgs.h>

## Description

The DataEventArgs provides information associated with a data event. Note that some properties are not available on every event.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DataEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [file](DataEventArgs_file.htm) | Gets the DataFile object associated with this event. If there isn't a DataFile associated with the event, this property will return null. |
| [filename](DataEventArgs_filename.htm) | Gets the filename associated with the operation. If there isn't an associated filename, an empty string is returned. For a download operation, this will be the full filename of the downloaded file. |
| [firingEvent](DataEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](DataEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [status](DataEventArgs_status.htm) | Returns a Status object that provides additional information about the success or failure of the operation. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |