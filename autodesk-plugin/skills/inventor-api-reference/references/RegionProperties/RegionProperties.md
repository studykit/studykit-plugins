# RegionProperties Object

## Description

The RegionProperties object. This object provides information relating to a profile region, including centroid, perimeter, rotation angle, moments of inertia, and axes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CentroidMomentsOfInertia](../RegionProperties/RegionProperties_CentroidMomentsOfInertia.md) | Method that returns the moments of inertia about the centroid of the section. |
| [GetTorsionProperties](../RegionProperties/RegionProperties_GetTorsionProperties.md) | Method that returns torsion coefficients of sketch profile. |
| [MomentsOfInertia](../RegionProperties/RegionProperties_MomentsOfInertia.md) | Method that returns the moments of inertia about the sketch origin. |
| [PrincipalAxes](../RegionProperties/RegionProperties_PrincipalAxes.md) | Method that returns the principal axes. |
| [PrincipalMomentsOfInertia](../RegionProperties/RegionProperties_PrincipalMomentsOfInertia.md) | Method that returns the moments of inertia about the principal axes. |
| [RadiusOfGyration](../RegionProperties/RegionProperties_RadiusOfGyration.md) | Method that returns the radius of gyration about the principal axes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Accuracy](../RegionProperties/RegionProperties_Accuracy.md) | Get and sets the desired accuracy of calculations. |
| [Application](../RegionProperties/RegionProperties_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Area](../RegionProperties/RegionProperties_Area.md) | Property that returns the area of the section in database units. |
| [Centroid](../RegionProperties/RegionProperties_Centroid.md) | Property that returns the centroid of the section. |
| [Parent](../RegionProperties/RegionProperties_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Perimeter](../RegionProperties/RegionProperties_Perimeter.md) | Property that returns the perimeter of the section in database units. |
| [RotationAngle](../RegionProperties/RegionProperties_RotationAngle.md) | Property that returns the angle of rotation of the principal axes. |
| [Type](../RegionProperties/RegionProperties_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Profile.RegionProperties](../Profile/Profile_RegionProperties.md), [ProfileProxy.RegionProperties](../ProfileProxy/ProfileProxy_RegionProperties.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Querying a sketch profile to get regions.](../../sample-programs/Profile_RegionProperties_Sample.md) | This sample demonstrates getting region properties from a sketch profile. |

## Version

Introduced in version 2008
