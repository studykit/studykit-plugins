# Documents Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Documents.h>

## Description

The Documents object provides access to all of the currently open documents and provides methods to create and open documents.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Documents_add.htm) | Creates and opens a new document of the specified type. |
| [classType](Documents_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Documents_item.htm) | Function that returns the specified document using an index into the collection. |
| [open](Documents_open.htm) | Opens an item that has previously been saved. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Documents_count.htm) | Returns the number of currently open documents. This includes documents that are visible and invisible. |
| [isValid](Documents_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Documents_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Application.documents](Application_documents.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |