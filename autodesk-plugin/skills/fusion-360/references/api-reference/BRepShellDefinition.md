# BRepShellDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinition.h>

## Description

Represents the definition of a B-Rep shell that can be used as input to create a BRepBody that includes this shell.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepShellDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [faceDefinitions](BRepShellDefinition_faceDefinitions.htm) | Provides access to the BRepFaceDefinitions object associated with this BRepShellDefinition. It's through the returned collection that you can create new BRepFaceDefinition objects. |
| [isValid](BRepShellDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepShellDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [wireDefinition](BRepShellDefinition_wireDefinition.htm) | Returns the single BRepWireDefinition associated with this shell definition. |

## Accessed From

[BRepShellDefinitions.add](BRepShellDefinitions_add.htm), [BRepShellDefinitions.item](BRepShellDefinitions_item.htm)

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