# Profiles3D Object

## Description

Provides access to all of the 3d profiles owned by a particular 3d sketch and supports the methods to create additional 3d profiles.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddClosed](../Profiles3D/Profiles3D_AddClosed.md) | Method that creates a new profile by examining the contents of the sketch and creating as many closed paths as possible. The resulting Profile3D is returned. |
| [AddOpen](../Profiles3D/Profiles3D_AddOpen.md) | Method that creates a new profile by examining the contents of the sketch for a set of connected entities and creating as many paths as possible. The paths may be open or closed. The resulting Profile3D is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Profiles3D/Profiles3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Profiles3D/Profiles3D_Count.md) | Property that returns the number of items in the collection. |
| [Item](../Profiles3D/Profiles3D_Item.md) | Method that returns the specified Profile3D object from the collection. |
| [Type](../Profiles3D/Profiles3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.Profiles3D](../Sketch3D/Sketch3D_Profiles3D.md), [Sketch3DProxy.Profiles3D](../Sketch3DProxy/Sketch3DProxy_Profiles3D.md)

## Version

Introduced in version 6
