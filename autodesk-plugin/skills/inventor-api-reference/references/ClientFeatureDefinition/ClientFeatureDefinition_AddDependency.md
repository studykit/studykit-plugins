# ClientFeatureDefinition.AddDependency Method

Parent Object: [ClientFeatureDefinition](../ClientFeatureDefinition/ClientFeatureDefinition.md)

## Description

Method that adds an upstream Inventor object as a dependency of the client feature.

## Remarks

Calling this method causes the OnClientFeatureSolve event for fire for this client feature if any of the dependents are recomputed. The IsCustomSolved flag must be set to True in order for the event to fire.

## Syntax

ClientFeatureDefinition.**AddDependency**( ***Dependency*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Dependency | Object | Input Object that specifies the dependency. This can be any of the following: Parameter, PartFeature, Sketch, Sketch3D, WorkPlane, WorkPoint, WorkAxis, DerivedPartComponent and DerivedAssemblyComponent. If a Parameter is input, the parameter is deleted when the client feature is deleted (unless the parameter has dependents other than the client feature). |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |