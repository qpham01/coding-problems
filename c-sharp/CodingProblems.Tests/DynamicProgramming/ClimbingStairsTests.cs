using CodingProblems.DynamicProgramming;

namespace CodingProblems.Tests.DynamicProgramming
{
    public class ClimbingStairsTests
    {
        private ClimbingStairs _sut;

        [SetUp]
        public void Setup()
        {
            _sut = new ClimbingStairs();
        }

        [TestCase(2, 2)]
        [TestCase(3, 3)]
        public void Test1(int steps, int ways)
        {
            var result = _sut.ClimbStairs(steps);
            Assert.That(result, Is.EqualTo(ways));
        }
    }
}