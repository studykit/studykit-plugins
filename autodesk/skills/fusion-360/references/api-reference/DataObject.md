# DataObject Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObject.h>

## Description

The DataObject provides access to the raw data that represents a logical entity. Typically, it is the bytes of a stored file, but it can also be something like the image data that could be stored within another file.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asString](DataObject_asString.htm) | Gets the file as a string (UTF-8). This is convenient when the saved file contains string data. For example, if the file contains JSON data. This eliminates the need to convert the Base64 string into a standard string. |
| [classType](DataObject_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getAsBase64String](DataObject_getAsBase64String.htm) | Gets the binary data represented by the DataObject as a Base64 encoded string. |
| [saveToFile](DataObject_saveToFile.htm) | Saves the data represented by the DataObject to a file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](DataObject_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataObject_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Component.createThumbnail](Component_createThumbnail.htm), [DataObjectFuture.dataObject](DataObjectFuture_dataObject.htm), [FlatPatternComponent.createThumbnail](FlatPatternComponent_createThumbnail.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |