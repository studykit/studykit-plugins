# NonParametricBaseFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The NonParametricBaseFeature object represents the feature that is created when a foreign file is translated into an Autodesk Inventor part file. If the foreign file defines a solid, it is read in and used to define the base feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../NonParametricBaseFeature/NonParametricBaseFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [DeleteFaces](../NonParametricBaseFeature/NonParametricBaseFeature_DeleteFaces.md) |  |
| [Edit](../NonParametricBaseFeature/NonParametricBaseFeature_Edit.md) | Edits the base feature. |
| [ExitEdit](../NonParametricBaseFeature/NonParametricBaseFeature_ExitEdit.md) | Exits the edit context of the base feature. |
| [GetReferenceKey](../NonParametricBaseFeature/NonParametricBaseFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../NonParametricBaseFeature/NonParametricBaseFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [Redefine](../NonParametricBaseFeature/NonParametricBaseFeature_Redefine.md) | Method that redefines the geometric contents of a non-parametric base feature. |
| [RemoveParticipant](../NonParametricBaseFeature/NonParametricBaseFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../NonParametricBaseFeature/NonParametricBaseFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../NonParametricBaseFeature/NonParametricBaseFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../NonParametricBaseFeature/NonParametricBaseFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../NonParametricBaseFeature/NonParametricBaseFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../NonParametricBaseFeature/NonParametricBaseFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../NonParametricBaseFeature/NonParametricBaseFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../NonParametricBaseFeature/NonParametricBaseFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../NonParametricBaseFeature/NonParametricBaseFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../NonParametricBaseFeature/NonParametricBaseFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../NonParametricBaseFeature/NonParametricBaseFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../NonParametricBaseFeature/NonParametricBaseFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../NonParametricBaseFeature/NonParametricBaseFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../NonParametricBaseFeature/NonParametricBaseFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputSurfaceBodies](../NonParametricBaseFeature/NonParametricBaseFeature_InputSurfaceBodies.md) | Property that returns the underlying SurfaceBody object associated with this feature. |
| [IsAssociative](../NonParametricBaseFeature/NonParametricBaseFeature_IsAssociative.md) | Property that indicates whether this contents of this base feature are associatively copied from bodies and faces in the assembly. |
| [IsComposite](../NonParametricBaseFeature/NonParametricBaseFeature_IsComposite.md) | Property that indicates if the non-parametric base feature is a composite of multiple solids and/or surfaces or is a single solid or surface. |
| [IsOwnedByFeature](../NonParametricBaseFeature/NonParametricBaseFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsSolid](../NonParametricBaseFeature/NonParametricBaseFeature_IsSolid.md) | Indicates whether this base feature is a solid or surface. |
| [Name](../NonParametricBaseFeature/NonParametricBaseFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../NonParametricBaseFeature/NonParametricBaseFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../NonParametricBaseFeature/NonParametricBaseFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../NonParametricBaseFeature/NonParametricBaseFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../NonParametricBaseFeature/NonParametricBaseFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../NonParametricBaseFeature/NonParametricBaseFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../NonParametricBaseFeature/NonParametricBaseFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../NonParametricBaseFeature/NonParametricBaseFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../NonParametricBaseFeature/NonParametricBaseFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../NonParametricBaseFeature/NonParametricBaseFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[NonParametricBaseFeatureProxy.NativeObject](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy_NativeObject.md), [NonParametricBaseFeatures.Add](../NonParametricBaseFeatures/NonParametricBaseFeatures_Add.md), [NonParametricBaseFeatures.AddByDefinition](../NonParametricBaseFeatures/NonParametricBaseFeatures_AddByDefinition.md), [NonParametricBaseFeatures.Item](../NonParametricBaseFeatures/NonParametricBaseFeatures_Item.md)

## Derived Classes

[NonParametricBaseFeatureProxy](../NonParametricBaseFeatureProxy/NonParametricBaseFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |

## Version

Introduced in version 5
