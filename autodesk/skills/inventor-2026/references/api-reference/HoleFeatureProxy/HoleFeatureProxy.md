# HoleFeatureProxy Object

Derived from: [HoleFeature](../HoleFeature/HoleFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../HoleFeatureProxy/HoleFeatureProxy_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../HoleFeatureProxy/HoleFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../HoleFeatureProxy/HoleFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../HoleFeatureProxy/HoleFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../HoleFeatureProxy/HoleFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../HoleFeatureProxy/HoleFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetCBore](../HoleFeatureProxy/HoleFeatureProxy_SetCBore.md) | Method that changes the hole to be a counterbore hole type. If the hole is already a counterbore type you can access and modify the counterbore parameters using the CBoreDiameter and CBoreDepth properties of the HoleFeature object. |
| [SetCSink](../HoleFeatureProxy/HoleFeatureProxy_SetCSink.md) | Method that changes the hole to be a countersink hole type. If the hole is already a countersink type you can access and modify the counterbore parameters using the CSinkDiameter and CSinkAngle properties of the HoleFeature object. |
| [SetDistanceExtent2](../HoleFeatureProxy/HoleFeatureProxy_SetDistanceExtent2.md) | Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as through all, which means it extends through all faces of the feature. This method defines th. |
| [SetDrilled](../HoleFeatureProxy/HoleFeatureProxy_SetDrilled.md) | Method that changes the hole to be a drilled hole type. |
| [SetEndOfPart](../HoleFeatureProxy/HoleFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSpotFace](../HoleFeatureProxy/HoleFeatureProxy_SetSpotFace.md) | Method that changes the hole to be a spotface hole type. If the hole is already a spotface type you can access and modify the spotface parameters using the SpotFaceDiameter and SpotFaceDepth properties of the HoleFeature object. This method will fail of the hole contains a tapered thread. |
| [SetSuppressionCondition](../HoleFeatureProxy/HoleFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetThroughAllExtent](../HoleFeatureProxy/HoleFeatureProxy_SetThroughAllExtent.md) | Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as "through all," which means it extends through all faces of the feature. This method defines a through-all termination type. |
| [SetToFaceExtent2](../HoleFeatureProxy/HoleFeatureProxy_SetToFaceExtent2.md) | Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as through all, which means it extends through all faces of the feature. This method defines th. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../HoleFeatureProxy/HoleFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../HoleFeatureProxy/HoleFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../HoleFeatureProxy/HoleFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../HoleFeatureProxy/HoleFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HoleFeatureProxy/HoleFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BottomTipAngle](../HoleFeatureProxy/HoleFeatureProxy_BottomTipAngle.md) | Property that returns the Parameter that defines the included angle of the tip of a blind hole, one that has been specified by a distance extent or 'to face' extent . If this is a Flat Bottomed hole then the property will return Nothing. |
| [CBoreDepth](../HoleFeatureProxy/HoleFeatureProxy_CBoreDepth.md) | Property that returns the parameter controlling the CBore depth. This property will return Nothing in the case where the HoleType is not kCounterBoreHole. |
| [CBoreDiameter](../HoleFeatureProxy/HoleFeatureProxy_CBoreDiameter.md) | Property that returns the parameter controlling the CBore diameter. This property will return Nothing in the case where the HoleType is not kCounterBoreHole. |
| [ClearanceInfo](../HoleFeatureProxy/HoleFeatureProxy_ClearanceInfo.md) | Gets and sets the HoleClearanceInfo object associated with the hole. |
| [ConsumeInputs](../HoleFeatureProxy/HoleFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../HoleFeatureProxy/HoleFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CSinkAngle](../HoleFeatureProxy/HoleFeatureProxy_CSinkAngle.md) | Property that returns the parameter controlling the CSink angle. This property will return Nothing in the case where the HoleType is not kCounterSinkHole. |
| [CSinkDepth](../HoleFeatureProxy/HoleFeatureProxy_CSinkDepth.md) | Gets depth of hole coutersink. |
| [CSinkDiameter](../HoleFeatureProxy/HoleFeatureProxy_CSinkDiameter.md) | Property that returns the parameter controlling the CSink diameter. This property will return Nothing in the case where the HoleType is not kCounterSinkHole. |
| [Depth](../HoleFeatureProxy/HoleFeatureProxy_Depth.md) | Gets depth of hole. |
| [DrillPointType](../HoleFeatureProxy/HoleFeatureProxy_DrillPointType.md) | Gets and sets hole drill point type. |
| [EndFaces](../HoleFeatureProxy/HoleFeatureProxy_EndFaces.md) | Property that returns the set of that cap the end of the hole. In the cases where there aren't any such end faces this property will return Nothing. |
| [ExtendedName](../HoleFeatureProxy/HoleFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [ExtendStart](../HoleFeatureProxy/HoleFeatureProxy_ExtendStart.md) | Gets and sets whether to extend the start of the hole feature.  When set this to True the hole feature will be extended to cut the body that is adjacent to the hole feature starting face. |
| [Extent](../HoleFeatureProxy/HoleFeatureProxy_Extent.md) | Property that returns the object that defines how the extent of the feature is defined. The type of extent object that this property will return can be determined by using the ExtentType property. |
| [ExtentType](../HoleFeatureProxy/HoleFeatureProxy_ExtentType.md) | Property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent property. |
| [Faces](../HoleFeatureProxy/HoleFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../HoleFeatureProxy/HoleFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../HoleFeatureProxy/HoleFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [HoleCenterPoints](../HoleFeatureProxy/HoleFeatureProxy_HoleCenterPoints.md) | Property that returns the set of points that define the centers of the holes of this feature. |
| [HoleDiameter](../HoleFeatureProxy/HoleFeatureProxy_HoleDiameter.md) | Property that returns the parameter controlling the diameter of the hole. This property will return Nothing if the diameter is being read off a value from the HoleTapInfo, when this hole is tapped. |
| [HoleType](../HoleFeatureProxy/HoleFeatureProxy_HoleType.md) | Property that returns the type of hole. Can be kDrilledHole, kCounterBoreHole, kCounterSinkHole, or kSpotFaceHole. The hole type can be set by using the SetCBore, SetCSink, SetDrilled, and SetSpotFace methods. |
| [IsClearanceHole](../HoleFeatureProxy/HoleFeatureProxy_IsClearanceHole.md) | Read – only property that returns the Boolean flag indicating whether the hole is clearance hole or not. |
| [IsOwnedByFeature](../HoleFeatureProxy/HoleFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../HoleFeatureProxy/HoleFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../HoleFeatureProxy/HoleFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../HoleFeatureProxy/HoleFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../HoleFeatureProxy/HoleFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../HoleFeatureProxy/HoleFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../HoleFeatureProxy/HoleFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PlacementDefinition](../HoleFeatureProxy/HoleFeatureProxy_PlacementDefinition.md) | Gets the Placement Definition for the hole feature. |
| [PlacementType](../HoleFeatureProxy/HoleFeatureProxy_PlacementType.md) | Property that returns a constant indicating the type of hole placement. |
| [RangeBox](../HoleFeatureProxy/HoleFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../HoleFeatureProxy/HoleFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../HoleFeatureProxy/HoleFeatureProxy_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [Sketch](../HoleFeatureProxy/HoleFeatureProxy_Sketch.md) | Property that returns the Sketch object that contains the points the hole is based on. |
| [SpotFaceDepth](../HoleFeatureProxy/HoleFeatureProxy_SpotFaceDepth.md) | Property that returns the parameter controlling the SpotFace depth. This property will return Nothing in the case where the HoleType is not kSpotFaceHole. |
| [SpotFaceDiameter](../HoleFeatureProxy/HoleFeatureProxy_SpotFaceDiameter.md) | Property that returns the parameter controlling the SpotFace diameter. This property will return Nothing in the case where the HoleType is not kSpotFaceHole. |
| [Suppressed](../HoleFeatureProxy/HoleFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../HoleFeatureProxy/HoleFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [TapInfo](../HoleFeatureProxy/HoleFeatureProxy_TapInfo.md) | Property that gets and sets the HoleTapInfo or TaperedThreadInfo object associated with the hole. |
| [Tapped](../HoleFeatureProxy/HoleFeatureProxy_Tapped.md) | Property that returns the Boolean flag indicating whether the hole is tapped or not. |
| [Type](../HoleFeatureProxy/HoleFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
