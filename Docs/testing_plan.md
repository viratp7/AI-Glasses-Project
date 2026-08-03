# Testing
## Test Name:
- Track ID test

## Purpose:
- To see if the newly prebuilt tracker can asssign stable ids to objects when they are slightly moving.

## Results:
- When the camera detects a non moving object like me, the tracking id stays consistent
- Moving camera test: For the most part tracking id stayed consistent and only displayed me, but the tracker detects things with low confidence or without a bounding box. This is a guess, based on the fact the tracker is assigning an id to something without a bounding box
- When testing with multiple objects same issue, but consistent id for the same object.

## Test Name:
- Multiple Same Object Test

## Purpose
- See if software can differentiate between two of the same objects and give them the same id.

## Results:
- The code is able to assign different id to two phones
- Issue was detecting the phones, may need specific optimization later.

