# ContourFlangeDefinition Object

## Description

The ContourFlangeDefinition object represents all of the information that defines a contour flange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddContourFlangeEdgeSet](../ContourFlangeDefinition/ContourFlangeDefinition_AddContourFlangeEdgeSet.md) | Method that adds a new contour flange edge set. The new FlangeEdgeSet is returned. This is applicable when the WidthExtentsFromSketchPlane is set to False. |
| [ContourFlangeEdgeSetItem](../ContourFlangeDefinition/ContourFlangeDefinition_ContourFlangeEdgeSetItem.md) | Method that returns the specified FlangeEdgeSet object from the collection. |
| [Copy](../ContourFlangeDefinition/ContourFlangeDefinition_Copy.md) | Method that creates a copy of this ContourFlangeDefinition object. |
| [SetDistanceExtent](../ContourFlangeDefinition/ContourFlangeDefinition_SetDistanceExtent.md) | Method that changes the ContourFlangeDefinition object to define a contour flange whose width is defined by a distance from the input Profile. |
| [SetDistanceWidthExtentTwo](../ContourFlangeDefinition/ContourFlangeDefinition_SetDistanceWidthExtentTwo.md) | Method that sets the second direction extent(Distance B) for the distance width extent of the ContourFlangeDefinition. |
| [SetFromToExtent](../ContourFlangeDefinition/ContourFlangeDefinition_SetFromToExtent.md) | Method that sets the width extent to define a contour flange whose width is defined as being between two entities. Calling this method will set WidthExtentsFromSketchPlane to True when the Operation is kJoinOperation. |
| [SetToExtent](../ContourFlangeDefinition/ContourFlangeDefinition_SetToExtent.md) | Method that sets the width extent to define a contour flange whose width is defined as being between original sketch plane and another entity. This is applicable when the WidthExtentsFromSketchPlane is True or when Operation is kJoinOperation. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../ContourFlangeDefinition/ContourFlangeDefinition_AffectedBodies.md) | Gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. |
| [Application](../ContourFlangeDefinition/ContourFlangeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ApplyAutoMitering](../ContourFlangeDefinition/ContourFlangeDefinition_ApplyAutoMitering.md) | Defines if auto mitering should be performed. |
| [BendEdges](../ContourFlangeDefinition/ContourFlangeDefinition_BendEdges.md) | Read-write property that gets and sets the EdgeCollection object that contains the edges that are used to define the adjoining edges for new face. This is applicable when the WidthExtentsFromSketchPlane property is True. |
| [BendExtensionType](../ContourFlangeDefinition/ContourFlangeDefinition_BendExtensionType.md) | Read-write property that gets and sets the bend extension type. This is applicable when the BendEdges is configured. |
| [BendOptions](../ContourFlangeDefinition/ContourFlangeDefinition_BendOptions.md) | Gets and sets the bend options associated with this contour flange feature. |
| [BendRadius](../ContourFlangeDefinition/ContourFlangeDefinition_BendRadius.md) | Gets and sets the bend radius of a contour flange feature. |
| [ContourFlangeEdgeSetCount](../ContourFlangeDefinition/ContourFlangeDefinition_ContourFlangeEdgeSetCount.md) | Read-only property that returns the contour flange edge set count currently defined in this contour flange definition. |
| [CornerOptions](../ContourFlangeDefinition/ContourFlangeDefinition_CornerOptions.md) | Gets and sets the CornerOptions object that defines how the corners of the contour flange are modeled. |
| [DistanceWidthExtentTwo](../ContourFlangeDefinition/ContourFlangeDefinition_DistanceWidthExtentTwo.md) | Read-only property that returns the PartFeatureExtent object that defines how the second distance width extent of the contour flange feature is defined. |
| [ExtentDirection](../ContourFlangeDefinition/ContourFlangeDefinition_ExtentDirection.md) | Gets and sets the extent direction which indicates which side of the sketch the projection of the flange is in. |
| [IsDistanceWidthExtentAsymmetric](../ContourFlangeDefinition/ContourFlangeDefinition_IsDistanceWidthExtentAsymmetric.md) | Read-only property that returns whether the distance width extent is asymmetric or not. |
| [IsUnfoldMethodOverridden](../ContourFlangeDefinition/ContourFlangeDefinition_IsUnfoldMethodOverridden.md) | Read-write property that gets and set whether the unfold method has been overridden for this feature. Setting this property to False clears the override. Setting the property to True returns a failure. |
| [MiterGap](../ContourFlangeDefinition/ContourFlangeDefinition_MiterGap.md) | Gets and sets the miter gap size of the Contour flange feature. |
| [Operation](../ContourFlangeDefinition/ContourFlangeDefinition_Operation.md) | Gets and sets the type of operation used to add the feature to the model. Valid inputs are kNewBodyOperation, kJoinOperation. |
| [Parent](../ContourFlangeDefinition/ContourFlangeDefinition_Parent.md) | Property that returns the parent ContourFlangeFeature of this ContourFlangeDefinition object. |
| [Path](../ContourFlangeDefinition/ContourFlangeDefinition_Path.md) | Gets and sets the Path object that defines the shape of the contour flange. |
| [SheetMetalRule](../ContourFlangeDefinition/ContourFlangeDefinition_SheetMetalRule.md) | Read-write property that gets and sets the sheet metal style for the body the feature is in. Set this property is applicable only when the feature is the first feature in a solid body. When set this property the default sheet metal rule will be overridden and. |
| [Type](../ContourFlangeDefinition/ContourFlangeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../ContourFlangeDefinition/ContourFlangeDefinition_UnfoldMethod.md) | Gets and sets the UnfoldMethod object that defines how the bends associated with this contour flange feature are unfolded. |
| [UseDefaultSheetMetalRule](../ContourFlangeDefinition/ContourFlangeDefinition_UseDefaultSheetMetalRule.md) | Read-write property that gets and sets whether to use the document active sheet metal style for the body the feature is in. Set this property is applicable only when the feature is the first feature in a solid body and this can only be set to True from False. |
| [WidthExtent](../ContourFlangeDefinition/ContourFlangeDefinition_WidthExtent.md) | Read-only property that returns the PartFeatureExtent object that defines how the width extent of the contour flange feature is defined. This is applicable when the WidthExtentsFromSketchPlane is True. |
| [WidthExtentsFromSketchPlane](../ContourFlangeDefinition/ContourFlangeDefinition_WidthExtentsFromSketchPlane.md) | Read-only property that get and sets the width extents type is from sketch plane or along selected edge. This is applicable when the Operation is kJoinOperation. |
| [WidthExtentType](../ContourFlangeDefinition/ContourFlangeDefinition_WidthExtentType.md) | Read-only property that returns the width extent type. The valid values for this property are kDistanceExten, kFromToExtent, and kToExtent. This is applicable when the WidthExtentsFromSketchPlane property is True. |

## Accessed From

[ContourFlangeDefinition.Copy](../ContourFlangeDefinition/ContourFlangeDefinition_Copy.md), [ContourFlangeFeature.Definition](../ContourFlangeFeature/ContourFlangeFeature_Definition.md), [ContourFlangeFeatureProxy.Definition](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy_Definition.md), [ContourFlangeFeatures.CreateDefinition](../ContourFlangeFeatures/ContourFlangeFeatures_CreateDefinition.md)

## Version

Introduced in version 2009
