# OnEdgeHolePositionDefinition Object

Derived from: [HolePositionDefinition](HolePositionDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OnEdgeHolePositionDefinition.h>

## Description

Provides positioning information for a hole that is positioned on the start, end or center of an edge.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OnEdgeHolePositionDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [edge](OnEdgeHolePositionDefinition_edge.htm) | Returns the edge the hole is positioned on. |
| [isValid](OnEdgeHolePositionDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](OnEdgeHolePositionDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [planarEntity](OnEdgeHolePositionDefinition_planarEntity.htm) | Returns the plane that defines the orientation and start of the hole. |
| [position](OnEdgeHolePositionDefinition_position.htm) | Returns the position of the hole on the edge. The hole can be at the start, midpoint, or end of the edge. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |