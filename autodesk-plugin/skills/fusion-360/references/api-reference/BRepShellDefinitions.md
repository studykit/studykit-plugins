# BRepShellDefinitions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShellDefinitions.h>

## Description

Provides access to the BRepShellDefinition objects associated with the object the collection was obtained from. It's through this object that you create new BRepShellDefinition objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BRepShellDefinitions_add.htm) | Creates a new empty BRepShellDefinition object associated with the parent BRepLumpDefinition. |
| [classType](BRepShellDefinitions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepShellDefinitions_item.htm) | Function that returns the specified BRepShellDefinition object using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepShellDefinitions_count.htm) | The number of B-Rep shell definition objects in the collection. |
| [isValid](BRepShellDefinitions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepShellDefinitions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepLumpDefinition.shellDefinitions](BRepLumpDefinition_shellDefinitions.htm)

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