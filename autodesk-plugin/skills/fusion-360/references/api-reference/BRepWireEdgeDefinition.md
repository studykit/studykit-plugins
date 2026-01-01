# BRepWireEdgeDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinition.h>

## Description

Represents the definition of an edge in B-Rep wire that can be used as input to create a BRepBody that includes this wire edge.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepWireEdgeDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [associativeID](BRepWireEdgeDefinition_associativeID.htm) | Gets and sets the associate ID of this B-Rep wire definition. This ID will be copied to the corresponding edge when the BRepBodyDefinition is used to create a BrepBody. It is used by Fusion as the identifier for the edge and is used for tracking this geometry for parametric recomputes. |
| [endVertex](BRepWireEdgeDefinition_endVertex.htm) | Gets and sets the end vertex of the wire edge definition. |
| [isValid](BRepWireEdgeDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [modelSpaceCurve](BRepWireEdgeDefinition_modelSpaceCurve.htm) | Gets and sets the Curve3D object that defines the shape of the edge using 3D geometry in model space. Valid objects are an Arc3D, NurbsCurve3D, Circle3D, Ellipse3D, EllipticalArc3D, or Line3D. |
| [objectType](BRepWireEdgeDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [startVertex](BRepWireEdgeDefinition_startVertex.htm) | Gets and sets the start vertex of the wire edge definition. |

## Accessed From

[BRepWireEdgeDefinitions.add](BRepWireEdgeDefinitions_add.htm), [BRepWireEdgeDefinitions.item](BRepWireEdgeDefinitions_item.htm)

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