# ModelSurfaceTextureSymbols.CreateDefinition Method

Parent Object: [ModelSurfaceTextureSymbols](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols.md)

## Description

Method that creates a surface texture symbol definition. This is a not a surface texture symbol but an object that encapsulates all of the information that defines a surface texture symbol. You use the methods and properties of this object to define the surface texture symbol you want to create and then provide it as input to the Add method.

## Syntax

ModelSurfaceTextureSymbols.**CreateDefinition**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) ) As [ModelSurfaceTextureSymbolDefinition](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection containing a series of Point objects representing the leader originating at the note. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating the geometry to attach the leader to. The ObjectCollection must contain at least one item, else the method will fail. The points are projected onto the orientation plane. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |

## Version

Introduced in version 2018
