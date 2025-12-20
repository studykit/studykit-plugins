# RectangularPatternFeatures.CreateDefinition Method

Parent Object: [RectangularPatternFeatures](../RectangularPatternFeatures/RectangularPatternFeatures.md)

## Description

Method that creates a new RectangularPatternFeatureDefinition object.

## Syntax

RectangularPatternFeatures.**CreateDefinition**( ***ParentFeatures*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***XDirectionEntity*** As Object, ***NaturalXDirection*** As Boolean, ***XCount*** As Variant, ***XSpacing*** As Variant, [***XSpacingType***] As [PatternSpacingTypeEnum](../PatternSpacingTypeEnum.md) ) As [RectangularPatternFeatureDefinition](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentFeatures | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the features or solids to be patterned. The collection could contain the various part features, sheet metal features, work planes, work axes, work points, or SurfaceBody objects. If SurfaceBody objects are supplied, the only other objects that can be in the collection are work planes, work axes, work points, and surface part features. |
| XDirectionEntity | Object | Input a linear entity that defines the first direction. This can be a linear Edge, a WorkAxis, a WorkPlane (normal is used), a planar Face (normal is used), or a GeometryIntent. When input GeometryIntent the geometry can be a non-linear Edge or Path, and the intent is used to specify a point on the geometry and the tangent direction at the point of the geometry will be used as the X-direction of the pattern feature.Use the CreatePath or CreateSpecifiedPath methods on the PartFeatures object to create a Path. The path can be a combination of 2D and 3D sketch elements. |
| NaturalXDirection | Boolean | Input Boolean that indicates if the direction of the pattern is in the natural direction of the XDirectionEntity or reversed. A value of True indicates it is in the natural direction. |
| XCount | Variant | Input Variant that defines the number of instances in the X direction. This can be either a numeric value or a string. A parameter will be created to control this value when the feature is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless number. |
| XSpacing | Variant | Input Variant that defines the spacing between instances in the X direction. This can be either a numeric value or a string. A parameter will be created to control this value when the feature is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless number. This input may be left unspecified only if the XSpacingType is kFitToPathLength and if the XDirectionEntity is not a work axis. |
| XSpacingType | [PatternSpacingTypeEnum](../PatternSpacingTypeEnum.md) | Optional input PatternSpacingTypeEnum enum that indicates if the occurrences along the x direction are to be fitted within a specified distance. A value of kDefault indicates that the occurrences are to be separated by the specified distance. A value of kFitted indicates that all occurrences are to be fitted within the specified distance. A value of kFitToPathLength indicates that all occurrences are to be fitted within a distance equal to the length of the XDirectionEntity. The kFitToPathLength value is invalid in cases where the XDirectionEntity is a work axis. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |