# CircularPatternFeatures.CreateDefinition Method

Parent Object: [CircularPatternFeatures](../CircularPatternFeatures/CircularPatternFeatures.md)

## Description

Method that creates a new CircularPatternFeatureDefinition object.

## Syntax

CircularPatternFeatures.**CreateDefinition**( ***ParentFeatures*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***AxisEntity*** As Object, ***NaturalAxisDirection*** As Boolean, ***Count*** As Variant, ***Angle*** As Variant, [***FitWithinAngle***] As Boolean ) As [CircularPatternFeatureDefinition](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentFeatures | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the features or solids to be patterned. The collection could contain the various part features, sheet metal features, work planes, work axes, work points, or SurfaceBody objects. If SurfaceBody objects are supplied, the only other objects that can be in the collection are work planes, work axes, work points, and surface part features. |
| AxisEntity | Object | Input a linear entity that defines the rotation axis. This can be a linear Edge, a WorkAxis, a cylindrical/conical/spherical/toroidal Face (axis is used). |
| NaturalAxisDirection | Boolean | Input Boolean that indicates if the direction of the pattern is in the natural direction of the AxisEntity or reversed. A value of True indicates it is in the natural direction. |
| Count | Variant | Input Variant that defines the number of instances in the pattern. This can be either a numeric value or a string. A parameter will be created to control this value when the feature is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless number. |
| Angle | Variant | Input Variant that defines the angle of the pattern. This can be either a numeric value or a string. A parameter will be created to control this value when the feature is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless value(document angular units will be used for it) or an angular unit value. |
| FitWithinAngle | Boolean | Optional input Boolean that defines how the count and angle are used to space the occurrences. If this property is true then the angle specifies the total sweep made by the pattern and the occurrences are evenly spaced within the angle. If it is false then the angle specifies the angular offset between each occurrence. This defaults to True. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |