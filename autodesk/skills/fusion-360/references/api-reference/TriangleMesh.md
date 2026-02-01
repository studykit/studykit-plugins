# TriangleMesh Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMesh.h>

## Description

The TriangleMesh object represents all of the data defining a triangular mesh.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TriangleMesh_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](TriangleMesh_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nodeCoordinates](TriangleMesh_nodeCoordinates.htm) | Returns the node coordinates as an array of Point3D objects. |
| [nodeCoordinatesAsDouble](TriangleMesh_nodeCoordinatesAsDouble.htm) | Returns the node coordinates as an array of doubles where they are the x, y, z components of each coordinate. |
| [nodeCoordinatesAsFloat](TriangleMesh_nodeCoordinatesAsFloat.htm) | Returns the node coordinates as an array of floats where they are the x, y, z components of each coordinate. |
| [nodeCount](TriangleMesh_nodeCount.htm) | Returns the total number of nodes in the mesh. |
| [nodeIndices](TriangleMesh_nodeIndices.htm) | Returns an array of indices that define which nodes are used for each triangle. This is used to look-up the coordinates in the NodeCoordinates array to get the three coordinates of each triangle. |
| [normalVectors](TriangleMesh_normalVectors.htm) | Returns the normal vectors of the mesh where there is a normal vector at each node. The normals are returned as an array of Vector3D objects. |
| [normalVectorsAsDouble](TriangleMesh_normalVectorsAsDouble.htm) | Returns the normal vectors of the mesh where there is a normal vector at each node. The normals are returned as an array of doubles where they are the x, y, z components of each vector. |
| [normalVectorsAsFloat](TriangleMesh_normalVectorsAsFloat.htm) | Returns the normal vectors of the mesh where there is a normal vector at each node. The normals are returned as an array of floats where they are the x, y, z components of each vector. |
| [objectType](TriangleMesh_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [surfaceTolerance](TriangleMesh_surfaceTolerance.htm) | Returns the surface tolerance that was used to generate this mesh. This is most useful when using display meshes that have already been calculated. |
| [textureCoordinates](TriangleMesh_textureCoordinates.htm) | Returns the texture coordinates used when mapping a texture to this face. The coordinates are returned as an array of Point2D objects where the x and y properties of the point are u and v coordinates as defined in parametric space. There is a texture coordinate for each vertex in the face mesh. |
| [textureCoordinatesAsDouble](TriangleMesh_textureCoordinatesAsDouble.htm) | Returns the texture coordinates used when mapping a texture to this face. The coordinates are returned as an array of doubles where they are the u and v components of each coordinate as defined in parametric space. There is a texture coordinate for each vertex in the face mesh. |
| [textureCoordinatesAsFloat](TriangleMesh_textureCoordinatesAsFloat.htm) | Returns the texture coordinates used when mapping a texture to this face. The coordinates are returned as an array of floats where they are the u and v components of each coordinate as defined in parametric space. There is a texture coordinate for each vertex in the face mesh. |
| [triangleCount](TriangleMesh_triangleCount.htm) | Returns the number of triangles in the mesh. |

## Accessed From

[MeshBody.displayMesh](MeshBody_displayMesh.htm), [TriangleMeshCalculator.calculate](TriangleMeshCalculator_calculate.htm), [TriangleMeshList.bestMesh](TriangleMeshList_bestMesh.htm), [TriangleMeshList.item](TriangleMeshList_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |