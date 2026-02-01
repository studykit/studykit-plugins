# BRepLumpDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumpDefinition.h>

## Description

Represents the definition of a B-Rep lump which is used in defining the topology of a B-Rep body.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepLumpDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](BRepLumpDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepLumpDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [shellDefinitions](BRepLumpDefinition_shellDefinitions.htm) | Provides access to the BRepShellDefinitions object associated with this BRepLumpDefinition. It's through the returned collection that you can create new BRepShellDefinition objects. |

## Accessed From

[BRepLumpDefinitions.add](BRepLumpDefinitions_add.htm), [BRepLumpDefinitions.item](BRepLumpDefinitions_item.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |