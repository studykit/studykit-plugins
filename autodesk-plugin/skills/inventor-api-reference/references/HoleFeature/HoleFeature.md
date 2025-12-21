# HoleFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The HoleFeature object represents hole modeling features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../HoleFeature/HoleFeature_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../HoleFeature/HoleFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../HoleFeature/HoleFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../HoleFeature/HoleFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../HoleFeature/HoleFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../HoleFeature/HoleFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetCBore](../HoleFeature/HoleFeature_SetCBore.md) | Method that changes the hole to be a counterbore hole type. If the hole is already a counterbore type you can access and modify the counterbore parameters using the CBoreDiameter and CBoreDepth properties of the HoleFeature object. |
| [SetCSink](../HoleFeature/HoleFeature_SetCSink.md) | Method that changes the hole to be a countersink hole type. If the hole is already a countersink type you can access and modify the counterbore parameters using the CSinkDiameter and CSinkAngle properties of the HoleFeature object. |
| [SetDistanceExtent2](../HoleFeature/HoleFeature_SetDistanceExtent2.md) | Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as through all, which means it extends through all faces of the feature. This method defines th. |
| [SetDrilled](../HoleFeature/HoleFeature_SetDrilled.md) | Method that changes the hole to be a drilled hole type. |
| [SetEndOfPart](../HoleFeature/HoleFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSpotFace](../HoleFeature/HoleFeature_SetSpotFace.md) | Method that changes the hole to be a spotface hole type. If the hole is already a spotface type you can access and modify the spotface parameters using the SpotFaceDiameter and SpotFaceDepth properties of the HoleFeature object. This method will fail of the hole contains a tapered thread. |
| [SetSuppressionCondition](../HoleFeature/HoleFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetThroughAllExtent](../HoleFeature/HoleFeature_SetThroughAllExtent.md) | Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as "through all," which means it extends through all faces of the feature. This method defines a through-all termination type. |
| [SetToFaceExtent2](../HoleFeature/HoleFeature_SetToFaceExtent2.md) | Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as through all, which means it extends through all faces of the feature. This method defines th. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../HoleFeature/HoleFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../HoleFeature/HoleFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../HoleFeature/HoleFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../HoleFeature/HoleFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HoleFeature/HoleFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BottomTipAngle](../HoleFeature/HoleFeature_BottomTipAngle.md) | Property that returns the Parameter that defines the included angle of the tip of a blind hole, one that has been specified by a distance extent or 'to face' extent . If this is a Flat Bottomed hole then the property will return Nothing. |
| [CBoreDepth](../HoleFeature/HoleFeature_CBoreDepth.md) | Property that returns the parameter controlling the CBore depth. This property will return Nothing in the case where the HoleType is not kCounterBoreHole. |
| [CBoreDiameter](../HoleFeature/HoleFeature_CBoreDiameter.md) | Property that returns the parameter controlling the CBore diameter. This property will return Nothing in the case where the HoleType is not kCounterBoreHole. |
| [ClearanceInfo](../HoleFeature/HoleFeature_ClearanceInfo.md) | Gets and sets the HoleClearanceInfo object associated with the hole. |
| [ConsumeInputs](../HoleFeature/HoleFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [CSinkAngle](../HoleFeature/HoleFeature_CSinkAngle.md) | Property that returns the parameter controlling the CSink angle. This property will return Nothing in the case where the HoleType is not kCounterSinkHole. |
| [CSinkDepth](../HoleFeature/HoleFeature_CSinkDepth.md) | Gets depth of hole coutersink. |
| [CSinkDiameter](../HoleFeature/HoleFeature_CSinkDiameter.md) | Property that returns the parameter controlling the CSink diameter. This property will return Nothing in the case where the HoleType is not kCounterSinkHole. |
| [Depth](../HoleFeature/HoleFeature_Depth.md) | Gets depth of hole. |
| [DrillPointType](../HoleFeature/HoleFeature_DrillPointType.md) | Gets and sets hole drill point type. |
| [EndFaces](../HoleFeature/HoleFeature_EndFaces.md) | Property that returns the set of that cap the end of the hole. In the cases where there aren't any such end faces this property will return Nothing. |
| [ExtendedName](../HoleFeature/HoleFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [ExtendStart](../HoleFeature/HoleFeature_ExtendStart.md) | Gets and sets whether to extend the start of the hole feature.  When set this to True the hole feature will be extended to cut the body that is adjacent to the hole feature starting face. |
| [Extent](../HoleFeature/HoleFeature_Extent.md) | Property that returns the object that defines how the extent of the feature is defined. The type of extent object that this property will return can be determined by using the ExtentType property. |
| [ExtentType](../HoleFeature/HoleFeature_ExtentType.md) | Property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent property. |
| [Faces](../HoleFeature/HoleFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../HoleFeature/HoleFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../HoleFeature/HoleFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [HoleCenterPoints](../HoleFeature/HoleFeature_HoleCenterPoints.md) | Property that returns the set of points that define the centers of the holes of this feature. |
| [HoleDiameter](../HoleFeature/HoleFeature_HoleDiameter.md) | Property that returns the parameter controlling the diameter of the hole. This property will return Nothing if the diameter is being read off a value from the HoleTapInfo, when this hole is tapped. |
| [HoleType](../HoleFeature/HoleFeature_HoleType.md) | Property that returns the type of hole. Can be kDrilledHole, kCounterBoreHole, kCounterSinkHole, or kSpotFaceHole. The hole type can be set by using the SetCBore, SetCSink, SetDrilled, and SetSpotFace methods. |
| [IsClearanceHole](../HoleFeature/HoleFeature_IsClearanceHole.md) | Read – only property that returns the Boolean flag indicating whether the hole is clearance hole or not. |
| [IsOwnedByFeature](../HoleFeature/HoleFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../HoleFeature/HoleFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../HoleFeature/HoleFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../HoleFeature/HoleFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../HoleFeature/HoleFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../HoleFeature/HoleFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PlacementDefinition](../HoleFeature/HoleFeature_PlacementDefinition.md) | Gets the Placement Definition for the hole feature. |
| [PlacementType](../HoleFeature/HoleFeature_PlacementType.md) | Property that returns a constant indicating the type of hole placement. |
| [RangeBox](../HoleFeature/HoleFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../HoleFeature/HoleFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../HoleFeature/HoleFeature_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [Sketch](../HoleFeature/HoleFeature_Sketch.md) | Property that returns the Sketch object that contains the points the hole is based on. |
| [SpotFaceDepth](../HoleFeature/HoleFeature_SpotFaceDepth.md) | Property that returns the parameter controlling the SpotFace depth. This property will return Nothing in the case where the HoleType is not kSpotFaceHole. |
| [SpotFaceDiameter](../HoleFeature/HoleFeature_SpotFaceDiameter.md) | Property that returns the parameter controlling the SpotFace diameter. This property will return Nothing in the case where the HoleType is not kSpotFaceHole. |
| [Suppressed](../HoleFeature/HoleFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../HoleFeature/HoleFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [TapInfo](../HoleFeature/HoleFeature_TapInfo.md) | Property that gets and sets the HoleTapInfo or TaperedThreadInfo object associated with the hole. |
| [Tapped](../HoleFeature/HoleFeature_Tapped.md) | Property that returns the Boolean flag indicating whether the hole is tapped or not. |
| [Type](../HoleFeature/HoleFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ConcentricHolePlacementDefinition.Parent](../ConcentricHolePlacementDefinition/ConcentricHolePlacementDefinition_Parent.md), [HoleFeatureProxy.NativeObject](../HoleFeatureProxy/HoleFeatureProxy_NativeObject.md), [HoleFeatures.AddCBoreByDistanceExtent2](../HoleFeatures/HoleFeatures_AddCBoreByDistanceExtent2.md), [HoleFeatures.AddCBoreByThroughAllExtent](../HoleFeatures/HoleFeatures_AddCBoreByThroughAllExtent.md), [HoleFeatures.AddCBoreByToFaceExtent2](../HoleFeatures/HoleFeatures_AddCBoreByToFaceExtent2.md), [HoleFeatures.AddCSinkByDistanceExtent2](../HoleFeatures/HoleFeatures_AddCSinkByDistanceExtent2.md), [HoleFeatures.AddCSinkByThroughAllExtent](../HoleFeatures/HoleFeatures_AddCSinkByThroughAllExtent.md), [HoleFeatures.AddCSinkByToFaceExtent2](../HoleFeatures/HoleFeatures_AddCSinkByToFaceExtent2.md), [HoleFeatures.AddDrilledByDistanceExtent2](../HoleFeatures/HoleFeatures_AddDrilledByDistanceExtent2.md), [HoleFeatures.AddDrilledByThroughAllExtent](../HoleFeatures/HoleFeatures_AddDrilledByThroughAllExtent.md), [HoleFeatures.AddDrilledByToFaceExtent2](../HoleFeatures/HoleFeatures_AddDrilledByToFaceExtent2.md), [HoleFeatures.AddSpotFaceByDistanceExtent2](../HoleFeatures/HoleFeatures_AddSpotFaceByDistanceExtent2.md), [HoleFeatures.AddSpotFaceByThroughAllExtent](../HoleFeatures/HoleFeatures_AddSpotFaceByThroughAllExtent.md), [HoleFeatures.AddSpotFaceByToFaceExtent2](../HoleFeatures/HoleFeatures_AddSpotFaceByToFaceExtent2.md), [HoleFeatures.Item](../HoleFeatures/HoleFeatures_Item.md), [HolePlacementDefinition.Parent](../HolePlacementDefinition/HolePlacementDefinition_Parent.md), [LinearHolePlacementDefinition.Parent](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_Parent.md), [PointHolePlacementDefinition.Parent](../PointHolePlacementDefinition/PointHolePlacementDefinition_Parent.md), [SketchHolePlacementDefinition.Parent](../SketchHolePlacementDefinition/SketchHolePlacementDefinition_Parent.md)

## Derived Classes

[HoleFeatureProxy](../HoleFeatureProxy/HoleFeatureProxy.md)

## Version

Introduced in version 5
