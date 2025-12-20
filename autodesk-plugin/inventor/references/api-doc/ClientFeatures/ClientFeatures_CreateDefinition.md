# ClientFeatures.CreateDefinition Method

Parent Object: [ClientFeatures](../ClientFeatures/ClientFeatures.md)

## Description

Method that creates a new ClientFeatureDefinition. The newly created ClientFeatureDefinition is returned.

## Syntax

ClientFeatures.**CreateDefinition**( [***FeatureType***] As String, [***StartElement***] As Variant, [***EndElement***] As Variant, [***FeatureInputs***] As Variant ) As [ClientFeatureDefinition](../ClientFeatureDefinition/ClientFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FeatureType | String | Optional input string that defines the naming of the client feature in the browser. If not specified, a default string 'ClientFeature' is used. |
| StartElement | Variant | Optional input object that specifies the first element to be composited in this feature. This object must correspond to a node in the browser. This can be a PartFeature, DerivedPartComponent, DerivedAssemblyComponent, iFeatureComponent, Sketch, Sketch3D, WorkPoint, WorkPlane, or a WorkAxis.   This is an optional argument whose default value is null. |
| EndElement | Variant | Optional input object that specifies the last element to be composited in this feature. This object must correspond to a node in the browser. An error occurs if the EndElement is not at the same level as the StartElement in the browser tree. If the StartElement argument is specified and this argument is not specified, the feature just composites the StartElement. If both StartElement and EndElement arguments are specified and they are the same, the feature just composites the StartElement. This argument is ignored if the StartElement argument is not specified. This can be a PartFeature, DerivedPartComponent, DerivedAssemblyComponent, iFeatureComponent, Sketch, Sketch3D, WorkPoint, WorkPlane, or a WorkAxis.   This is an optional argument whose default value is null. |
| FeatureInputs | Variant | Optional input ObjectCollection that specifies the inputs use to create this feature. The inputs are currently limited to 2D & 3D sketches. The inputs must be above the feature in the browser. When sketches are specified as inputs, the behavior is the same as a regular Inventor feature (such as Extrude) consuming a sketch. The sketch appears under the client feature and can be 'shared' by the user so it is usable in other downstream features. The input objects are not 'strongly owned' by the client feature. i.e. when the client feature is deleted, the user has the option to retain the feature inputs. The feature inputs do not highlight with the client feature.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |