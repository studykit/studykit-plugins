# NonParametricBaseFeatureProxy Object

Derived from: [NonParametricBaseFeature](../NonParametricBaseFeature/NonParametricBaseFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [DeleteFaces](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_DeleteFaces.md) |  |
| [Edit](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Edit.md) | Edits the base feature. |
| [ExitEdit](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_ExitEdit.md) | Exits the edit context of the base feature. |
| [GetReferenceKey](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [Redefine](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Redefine.md) | Method that redefines the geometric contents of a non-parametric base feature. |
| [RemoveParticipant](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputSurfaceBodies](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_InputSurfaceBodies.md) | Property that returns the underlying SurfaceBody object associated with this feature. |
| [IsAssociative](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_IsAssociative.md) | Property that indicates whether this contents of this base feature are associatively copied from bodies and faces in the assembly. |
| [IsComposite](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_IsComposite.md) | Property that indicates if the non-parametric base feature is a composite of multiple solids and/or surfaces or is a single solid or surface. |
| [IsOwnedByFeature](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsSolid](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_IsSolid.md) | Indicates whether this base feature is a solid or surface. |
| [Name](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
