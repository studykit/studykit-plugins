# BRepCoEdgeDefinitions Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinitions.h>

## Description

Provides access to the BRepCoEdgeDefinition objects associated with the parent BRepLoopDefinition object. It's through this object that you create new BRepCoEdgeDefinition objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BRepCoEdgeDefinitions_add.htm) | Creates a new BrepCoEdgeDefinition object associated with the parent BrepLoopDefinition object. |
| [classType](BRepCoEdgeDefinitions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepCoEdgeDefinitions_item.htm) | Function that returns the specified BRepCoEdgeDefinition object using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepCoEdgeDefinitions_count.htm) | The number of B-Rep co-edge definition objects in the collection. |
| [isValid](BRepCoEdgeDefinitions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepCoEdgeDefinitions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepLoopDefinition.bRepCoEdgeDefinitions](BRepLoopDefinition_bRepCoEdgeDefinitions.htm)

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |