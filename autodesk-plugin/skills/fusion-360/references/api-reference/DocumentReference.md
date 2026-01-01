# DocumentReference Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReference.h>

## Description

Represents a reference to a document from another document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DocumentReference_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getLatestVersion](DocumentReference_getLatestVersion.htm) | Updates the reference to use the latest version. This is only useful when the isOutOfDate property is true. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dataFile](DocumentReference_dataFile.htm) | The dataFile on A360 that this object references. |
| [isOutOfDate](DocumentReference_isOutOfDate.htm) | Indicates if this reference is out of date, meaning that the reference is not referencing the latest version. |
| [isValid](DocumentReference_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DocumentReference_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentDocument](DocumentReference_parentDocument.htm) | The document that is doing the referencing and owns this reference. |
| [referencedDocument](DocumentReference_referencedDocument.htm) | The document currently open in Fusion that this object references. |
| [version](DocumentReference_version.htm) | Gets and sets the version of the dataFile on A360 that this document currently represents. Setting this property will cause all occurrences referencing this document to update to that version. |

## Accessed From

[DocumentReferences.item](DocumentReferences_item.htm), [Occurrence.documentReference](Occurrence_documentReference.htm)

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |