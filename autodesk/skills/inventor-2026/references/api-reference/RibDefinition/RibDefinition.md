# RibDefinition Object

## Description

RibDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../RibDefinition/RibDefinition_Copy.md) | Method that creates a copy of this RibDefinition object. The new RibDefinition object is independent of any feature. It can be edited and used as input to edit an existing feature or to create a new Rib feature.  One typical use of this method is when you need to make several changes to an existing Rib feature. If you edit the RibDefinition object associated with the Rib feature, the feature will recompute after each edit. It’s more efficient to make a copy, edit the copy, and then assign the copy to the feature. This will result in a single recompute.  The RibFeatures.CreateDefinition method can also be used to create an independent RibDefinition object. The difference is that one created with the Copy method will have the same initial values as the object is was copied from. One that’s created with the CreateDefinition method will be initialized to predefined default values. |
| [GetThicknessPlane](../RibDefinition/RibDefinition_GetThicknessPlane.md) | Method that gets the plane at which the input thickness is held. |
| [SetFiniteExtent](../RibDefinition/RibDefinition_SetFiniteExtent.md) | Method that sets the extent type to be a finite distance. |
| [SetThicknessPlane](../RibDefinition/RibDefinition_SetThicknessPlane.md) | Method that sets the plane at which the input thickness is held. |
| [SetToNextExtent](../RibDefinition/RibDefinition_SetToNextExtent.md) | Method that sets the extent type to be ‘to next’ (i.e. it terminates on the next face). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBody](../RibDefinition/RibDefinition_AffectedBody.md) | Read-write property that gets and sets the solid body affected by the creation of this rib feature. For parts containing multiple solid bodies, this property defaults to the primary solid body of the part, and can be set to any of the other solid bodies. |
| [Application](../RibDefinition/RibDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BossSets](../RibDefinition/RibDefinition_BossSets.md) | Read-only property that returns the BossSets collection object containing boss definitions of the rib feature. |
| [DirectionReversed](../RibDefinition/RibDefinition_DirectionReversed.md) | Read-write property that gets and sets whether the direction of the profile projection should be reversed. If the profile is projected normal to the sketch plane, setting this property to True causes the profile to be projected in the reverse direction of the. |
| [DraftAngle](../RibDefinition/RibDefinition_DraftAngle.md) | Read-write property that provides access to the taper angle of a rib feature. This property is writable when the RibDefinition object has been created using the RibFeatures.CreateDefinition or RibDefinition.Copy methods. |
| [DraftProfileEnds](../RibDefinition/RibDefinition_DraftProfileEnds.md) | Read-write property that gets and sets the draft profile ends value. |
| [ExtendProfile](../RibDefinition/RibDefinition_ExtendProfile.md) | Read-write property that gets and sets whether the rib profile should be extended/trimmed to intersect faces, if necessary. This property defaults to True for a newly created RibDefinition object. |
| [ExtentDistance](../RibDefinition/RibDefinition_ExtentDistance.md) | Read-only property that returns the parameter that corresponds to the distance value for rib feature defined with a finite extent. This property returns a parameter only if the ExtentType is kFiniteRibExtent, else this property returns Nothing. Also, in the case where this is a newly created RibDefinition object or it has been copied from an existing RibDefinition object, this property returns Nothing since there isn’t a parameter created yet. |
| [ExtentType](../RibDefinition/RibDefinition_ExtentType.md) | Read-only property that returns the extent type of the rib feature. The possible return values are kFiniteRibExtent and kToNextRibExtent. When the RibDefinition object is initially created, this defaults to kToNextRibExtent. If this property returns kFiniteRibExtent, the ExtentDistance property returns the correspond parameter. Use the SetFiniteExtent and Set ToNextExtent methods to edit the extent type. |
| [IsRib](../RibDefinition/RibDefinition_IsRib.md) | Read-write property that gets and sets whether the sketch profile is projected lateral to the sketch plane (rib) or normal to the sketch plane (web) to create the feature. A value of True indicates that the profile is projected lateral to the sketch plane. |
| [Parent](../RibDefinition/RibDefinition_Parent.md) | Read-only property that returns the parent RibFeature of this RibDefinition object. In the case where this is a newly created RibDefinition object or it has been copied from an existing RibDefinition object, this property will return Nothing because there is not a logical parent for the object. |
| [ProfileCurves](../RibDefinition/RibDefinition_ProfileCurves.md) | Read-write property that gets and sets the collection of sketch entities used as the profile for feature creation. |
| [Thickness](../RibDefinition/RibDefinition_Thickness.md) | Read-write property that provides access to the thickness of the feature. This property is writable when the RibDefinition object has been created using the RibFeatures.CreateDefinition or RibDefinition.Copy methods. The value can be set using either a doubl. |
| [ThicknessDirection](../RibDefinition/RibDefinition_ThicknessDirection.md) | Read-write property that gets and sets the side of the profile on which to apply the thickness. This property defaults to kSymmetricExtentDirection for a newly created RibDefinition object. |
| [Type](../RibDefinition/RibDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BossSet.Parent](../BossSet/BossSet_Parent.md), [RibDefinition.Copy](../RibDefinition/RibDefinition_Copy.md), [RibFeature.Definition](../RibFeature/RibFeature_Definition.md), [RibFeatureProxy.Definition](../RibFeatureProxy/RibFeatureProxy_Definition.md), [RibFeatures.CreateDefinition](../RibFeatures/RibFeatures_CreateDefinition.md)

## Version

Introduced in version 2012
