# TemporaryBRepManager Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

A utility object that provides functionality to create and manipulate B-Rep data outside the context of a document. The provides direct access to the modeling core without the overhead of parametrics, persistence, transactions, or graphics. It also provides a way of directly defining and creating B-Rep data.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [booleanOperation](TemporaryBRepManager_booleanOperation.htm) | Performs the specified Boolean operation between the two input bodies. The input bodies need not be solid but can be faces that are combined or trimmed. |
| [classType](TemporaryBRepManager_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](TemporaryBRepManager_copy.htm) | Creates a temporary copy of the input BRepBody, BRepFace, or BRepEdge object. |
| [createBox](TemporaryBRepManager_createBox.htm) | Creates a new temporary solid box BRepBody object. |
| [createCylinderOrCone](TemporaryBRepManager_createCylinderOrCone.htm) | Creates a temporary solid cylinder or cone BRepBody object. |
| [createEllipticalCylinderOrCone](TemporaryBRepManager_createEllipticalCylinderOrCone.htm) | Creates a temporary elliptical solid cylinder or cone BrepBody object. |
| [createFaceFromPlanarWires](TemporaryBRepManager_createFaceFromPlanarWires.htm) | Creates a body from multiple wires that all lie within the same plane. Multiple wires are used when creating a plane with interior holes. One wire defines the outer shape and the other wires define the interior loops of the created face. |
| [createFromFile](TemporaryBRepManager_createFromFile.htm) | Creates new BRepBody objects based on the contents of the specified file. |
| [createHelixWire](TemporaryBRepManager_createHelixWire.htm) | Creates a B-Rep body that contains a wire with a single edge that represents a helical curve. |
| [createProjectedBodyOutline](TemporaryBRepManager_createProjectedBodyOutline.htm) | Computes the approximate outline of a body. The outline is the loops formed from projecting the non-occluded silhouette curves of the body onto a plane. The outline is returned as a temporary BRepBody consisting of planar BRepFace objects whose boundaries form the outline. |
| [createRuledSurface](TemporaryBRepManager_createRuledSurface.htm) | Creates a new body by creating a ruled surface between the two input wire bodies. |
| [createSilhouetteCurves](TemporaryBRepManager_createSilhouetteCurves.htm) | Calculates the silhouette curve geometry for a given face as viewed from a given direction. |
| [createSphere](TemporaryBRepManager_createSphere.htm) | Creates a temporary spherical BRepBody object. |
| [createTorus](TemporaryBRepManager_createTorus.htm) | Creates a temporary toroidal BRepBody object. |
| [createWireFromCurves](TemporaryBRepManager_createWireFromCurves.htm) | Give an array of curve geometry objects, this method creates a new wire body. |
| [deleteFaces](TemporaryBRepManager_deleteFaces.htm) | Deletes one or more faces from a temporary BRepBody. The body that will be modified is determined by getting the parent body of the input faces. |
| [exportToFile](TemporaryBRepManager_exportToFile.htm) | Exports the input bodies to the specified file. |
| [get](TemporaryBRepManager_get.htm) | Gets the TempoaryBRepManager object. This object provides access to functionality to create an manipulate temporary B-Rep data outside the context of a document. |
| [imprintOverlapBodies](TemporaryBRepManager_imprintOverlapBodies.htm) | Method that finds regions of faces on two bodies which overlap and creates new bodies where the faces are split at the edges of the overlaps. This does not modify the original bodies but creates new temporary bodies that contain the imprints. |
| [planeIntersection](TemporaryBRepManager_planeIntersection.htm) | Calculates the intersection between the input body and plane and creates a wire body that represents the intersection curves. |
| [transform](TemporaryBRepManager_transform.htm) | Transforms the input body using the specified transformation matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](TemporaryBRepManager_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TemporaryBRepManager_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[TemporaryBRepManager.get](TemporaryBRepManager_get.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |