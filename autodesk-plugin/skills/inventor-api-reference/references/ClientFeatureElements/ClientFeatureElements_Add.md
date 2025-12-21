# ClientFeatureElements.Add Method

Parent Object: [ClientFeatureElements](../ClientFeatureElements/ClientFeatureElements.md)

## Description

Method that adds an element to the client feature definition and returns a ClientFeatureElement object.

## Syntax

ClientFeatureElements.**Add**( ***Element*** As Object, [***BrowserVisible***] As Boolean ) As [ClientFeatureElement](../ClientFeatureElement/ClientFeatureElement.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Element | Object | Input Object that specifies an object to add to the client feature. The input object must correspond to a node in the browser tree. This method fails if the input object is not adjacent to the client feature in the browser tree in the case where the client feature already composites certain elements. If the ClientFeature does not already composite any native object, the ClientFeature is moved to the position of the element in the browser. This can be a PartFeature, DerivedPartComponent, DerivedAssemblyComponent, iFeatureComponent, Sketch, Sketch3D, WorkPoint, WorkPlane, or a WorkAxis. |
| BrowserVisible | Boolean | Optional input Boolean that indicates whether this element is visible in the browser under the client feature node. If not specified, the argument defaults to False. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |