/*
  Warnings:

  - Changed the type of `configuration` on the `Component` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.
  - Changed the type of `configuration` on the `Product` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "Component" DROP COLUMN "configuration",
ADD COLUMN     "configuration" INTEGER NOT NULL;

-- AlterTable
ALTER TABLE "Product" DROP COLUMN "configuration",
ADD COLUMN     "configuration" INTEGER NOT NULL;
