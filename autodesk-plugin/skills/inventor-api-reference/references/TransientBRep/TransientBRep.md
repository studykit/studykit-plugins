# TransientBRep Object

## Description

The TransientBRep object is used to create and manipulate B-Rep objects within a transient space.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../TransientBRep/TransientBRep_Copy.md) | Method that creates a copy of the input SurfaceBody, Face, or Edge object. |
| [CreateIntersectionWithPlane](../TransientBRep/TransientBRep_CreateIntersectionWithPlane.md) | Method that intersects a body with a plane. |
| [CreateRuledSurface](../TransientBRep/TransientBRep_CreateRuledSurface.md) | Method that creates a ruled surface between the two sections. |
| [CreateSilhouetteCurve](../TransientBRep/TransientBRep_CreateSilhouetteCurve.md) | Method that calculates the silhouette curve geometry for a given face as viewed from a given direction. |
| [CreateSolidBlock](../TransientBRep/TransientBRep_CreateSolidBlock.md) | Method that creates a solid box. |
| [CreateSolidCylinderCone](../TransientBRep/TransientBRep_CreateSolidCylinderCone.md) | Method that create a solid cylinder or cone. |
| [CreateSolidSphere](../TransientBRep/TransientBRep_CreateSolidSphere.md) | Method that create a solid sphere. |
| [CreateSolidTorus](../TransientBRep/TransientBRep_CreateSolidTorus.md) | Method that creates a solid torus. |
| [CreateSurfaceBodyDefinition](../TransientBRep/TransientBRep_CreateSurfaceBodyDefinition.md) | Method that creates a new SurfaceBodyDefinition object. |
| [DeleteFaces](../TransientBRep/TransientBRep_DeleteFaces.md) | Method that modifies an existing transient surface body by deleting specified faces. |
| [DoBoolean](../TransientBRep/TransientBRep_DoBoolean.md) | Method that performs the specified Boolean operation between the blank and tool bodies. |
| [GetIdenticalBodies](../TransientBRep/TransientBRep_GetIdenticalBodies.md) | Method that find the identical SurfaceBody objects in a SurfaceBody objects collection. In the return value, all the identical surface bodies will be placed in the same ObjectCollection. |
| [ImprintBodies](../TransientBRep/TransientBRep_ImprintBodies.md) | Method that finds regions of faces on two bodies which overlap and creates new bodies where the faces are split at the edges of the overlaps. This does not modify the original bodies but creates new transient bodies that contain the imprints. |
| [ReadFromFile](../TransientBRep/TransientBRep_ReadFromFile.md) | Method that creates one or more new SurfaceBody objects based on the content of the input file. A SurfaceBodies collection is returned that can contain one or more SurfaceBody object. |
| [Transform](../TransientBRep/TransientBRep_Transform.md) | Method that transforms the input SurfaceBody. |
| [WriteToFile](../TransientBRep/TransientBRep_WriteToFile.md) | Writes out the specified bodies as a file. |

## Accessed From

[Application.TransientBRep](../Application/Application_TransientBRep.md), [InventorServer.TransientBRep](InventorServer_TransientBRep.md), [InventorServerObject.TransientBRep](InventorServerObject_TransientBRep.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics from SAT file body](../../sample-programs/GraphicsNode_AddSurfaceGraphics_Sample.md) | The following sample demonstrates how to display client graphics based on bodies read in from a SAT file. |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2009
