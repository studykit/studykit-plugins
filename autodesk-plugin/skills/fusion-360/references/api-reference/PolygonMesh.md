# PolygonMesh Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/PolygonMesh.h>

## Description

The PolygonMesh represents a mesh that can contain any combination of polygons, quads, and triangles.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PolygonMesh_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](PolygonMesh_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nodeCoordinates](PolygonMesh_nodeCoordinates.htm) | Returns the node coordinates as an array of Point3D objects. |
| [nodeCoordinatesAsDouble](PolygonMesh_nodeCoordinatesAsDouble.htm) | Returns the node coordinates as an array of doubles where they are the x, y, z components of each coordinate. |
| [nodeCoordinatesAsFloat](PolygonMesh_nodeCoordinatesAsFloat.htm) | Returns the node coordinates as an array of floats where they are the x, y, z components of each coordinate. |
| [nodeCount](PolygonMesh_nodeCount.htm) | Returns the number of nodes in the mesh. |
| [nodeCountPerPolygon](PolygonMesh_nodeCountPerPolygon.htm) | Returns the number of nodes that define each polygon. For example, if NodeCountPerPolygon[0] returns 6 it indicates the first polygon is defined using 6 nodes. The first six indices returned by the PolygonNodeIndices properties provide the look-up into the NodeCoordinates array. |
| [normalVectors](PolygonMesh_normalVectors.htm) | Returns the normal vectors as an array of Vector 3D objects. There is one normal vector for each index. |
| [normalVectorsAsDouble](PolygonMesh_normalVectorsAsDouble.htm) | Returns the normal vectors as an array of doubles where they are the x, y, z components of each vector. There is one normal vector for each index. |
| [normalVectorsAsFloat](PolygonMesh_normalVectorsAsFloat.htm) | Returns the normal vectors as an array of floats. There is one normal vector for each index. |
| [objectType](PolygonMesh_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [polygonCount](PolygonMesh_polygonCount.htm) | Returns the number of polygons (more than 4 sides) in the mesh. |
| [polygonNodeIndices](PolygonMesh_polygonNodeIndices.htm) | Returns the index values that index into the NodeCoordinates and NormalVectors arrays to define the coordinates of each polygon and the corresponding normal. |
| [quadCount](PolygonMesh_quadCount.htm) | Returns the number of quads in the mesh. |
| [quadNodeIndices](PolygonMesh_quadNodeIndices.htm) | Returns the index values that index into the NodeCoordinates and NormalVectors arrays to define the four coordinates of each quad and the corresponding normal. |
| [triangleCount](PolygonMesh_triangleCount.htm) | Returns the number of triangles in the mesh. |
| [triangleFaceGroupTempIds](PolygonMesh_triangleFaceGroupTempIds.htm) | ![Preview](../images/TestTubeSmall.png)Returns the face groups tempId values for every triangle of the mesh. The tempId corresponds to the triangles, which are defined in triangleNodeIndices. |
| [triangleNodeIndices](PolygonMesh_triangleNodeIndices.htm) | Returns the index values that index into the NodeCoordinates and NormalVectors arrays to define the three coordinates of each triangle and the corresponding normal. |
| [wallThickness](PolygonMesh_wallThickness.htm) | ![Preview](../images/TestTubeSmall.png)Returns the wall thickness per node in cm. This property calculates the wall thickness of the mesh, i.e. the distance of a surface of the mesh to the opposing surface. |

## Accessed From

[MeshBody.mesh](MeshBody_mesh.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |