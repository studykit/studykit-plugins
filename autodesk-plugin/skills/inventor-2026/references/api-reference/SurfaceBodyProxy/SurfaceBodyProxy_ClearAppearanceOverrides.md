# SurfaceBodyProxy.ClearAppearanceOverrides Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Method that clears all the appearance overrides that have been applied to faces or features in the body. When the SurfaceBody has its IsSolid return True, this method sets the AppearanceSourceType to kBodyAppearance for all the features and kFeatureAppearance for all the faces in the body. When the SurfaceBody has its IsSolid return False, this method sets the AppearanceSourceType to kBodyAppearance for all the features directly owned by the work surface and kFeatureAppearance for all the faces in the body.

## Syntax

SurfaceBodyProxy.**ClearAppearanceOverrides**()

## Version

Introduced in version 2014
