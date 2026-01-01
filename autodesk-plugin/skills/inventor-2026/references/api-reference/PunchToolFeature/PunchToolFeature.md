# PunchToolFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The PunchToolFeature object represents the instance of a placed punch tool feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PunchToolFeature/PunchToolFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../PunchToolFeature/PunchToolFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../PunchToolFeature/PunchToolFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../PunchToolFeature/PunchToolFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../PunchToolFeature/PunchToolFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../PunchToolFeature/PunchToolFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../PunchToolFeature/PunchToolFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AcrossBends](../PunchToolFeature/PunchToolFeature_AcrossBends.md) | Gets and sets the property that defines the across bends. |
| [Adaptive](../PunchToolFeature/PunchToolFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Angle](../PunchToolFeature/PunchToolFeature_Angle.md) | Property that returns the parameter object that controls the angle of rotation of the punch tool. |
| [Appearance](../PunchToolFeature/PunchToolFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../PunchToolFeature/PunchToolFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../PunchToolFeature/PunchToolFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PunchToolFeature/PunchToolFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../PunchToolFeature/PunchToolFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Depth](../PunchToolFeature/PunchToolFeature_Depth.md) | Property that returns the parameter object that defines the custom punch depth. |
| [ExtendedName](../PunchToolFeature/PunchToolFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../PunchToolFeature/PunchToolFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../PunchToolFeature/PunchToolFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../PunchToolFeature/PunchToolFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iFeatureDefinition](../PunchToolFeature/PunchToolFeature_iFeatureDefinition.md) | Gets and sets the associated iFeatureDefinition. |
| [iFeatureTemplateDescriptor](../PunchToolFeature/PunchToolFeature_iFeatureTemplateDescriptor.md) | Property that returns the iFeatureTemplateDescriptor object associated with this iFeature. |
| [IsOwnedByFeature](../PunchToolFeature/PunchToolFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../PunchToolFeature/PunchToolFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../PunchToolFeature/PunchToolFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../PunchToolFeature/PunchToolFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../PunchToolFeature/PunchToolFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../PunchToolFeature/PunchToolFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PunchCenterPoints](../PunchToolFeature/PunchToolFeature_PunchCenterPoints.md) | Gets and sets the set of sketch points that define the origin points for the punch tool. |
| [PunchRepresentationType](../PunchToolFeature/PunchToolFeature_PunchRepresentationType.md) | Gets and sets punch tool feature representation type. |
| [RangeBox](../PunchToolFeature/PunchToolFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../PunchToolFeature/PunchToolFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../PunchToolFeature/PunchToolFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../PunchToolFeature/PunchToolFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../PunchToolFeature/PunchToolFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldInFlatPattern](../PunchToolFeature/PunchToolFeature_UnfoldInFlatPattern.md) | Read-write property that gets and sets whether the punch tool feature is unfoldable in flat pattern. |

## Accessed From

[PunchToolFeatures.Add](../PunchToolFeatures/PunchToolFeatures_Add.md), [PunchToolFeatures.Item](../PunchToolFeatures/PunchToolFeatures_Item.md)

## Derived Classes

[PunchToolFeatureProxy](../PunchToolFeatureProxy/PunchToolFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Report on punch feature ID's](../../sample-programs/PunchToolFeatureIDs_Sample.md) | This program demonstrates accessing punch features and creates a report of the punch ID's used. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |

## Version

Introduced in version 5.3
